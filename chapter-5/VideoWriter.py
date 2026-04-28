# for Colab
!pip install ffmpeg-python
from google.colab.output import eval_js
from IPython.display import display, Javascript

import ffmpeg
from base64 import b64decode

def VideoWriter(out_file, duration, frame_rate, wh):
	# Colabで動画撮影・保存
	# 本 p.151 "cv2.VideoWriter" の代用
	# 通常の動画撮影用, タイムラプス撮影はできない

	_js = """
		const outputArea = document.querySelector("#output-area");
		const video = document.createElement("video");
		const info = document.createElement("p");
		let blob = null
		let durationMsec = null

		async function record(durationSec, frameRate, width, height) {
			durationMsec = durationSec * 10**3;
			const browser = navigator.mediaDevices;
			const supported = browser.getSupportedConstraints();
			if (!supported.width || !supported.height || !supported.frameRate) {
				throw new Error("Browser is not supported for width, height or frameRate.");
			}
			const stream = await browser.getUserMedia({
				video: {
					width,
					height,
					frameRate,
						// Chrome: width/heightの挙動が変(v146) ex.720x480を指定すると1024x684になる
						// Firefox: frameRateの挙動が変(v149) ex.15を指定すると60になる
						// c.f. https://developer.mozilla.org/ja/docs/Web/API/MediaDevices/getUserMedia
				},
				audio: false,
			});
			startDisplay(stream);
			const result = await recordCore(stream, {
				// mimeType: "video/mp4" // error on Firefox
			});
			stopDisplay();
			return result;
		}

		async function recordCore(stream, options) {
			const mediaRecorder = new MediaRecorder(stream, options);
			mediaRecorder.addEventListener(
				"dataavailable", e => {
					// fired on mediaRecorder.stop
					blob = e.data;
				}
			);
			mediaRecorder.start();
			await new Promise(resolve => setTimeout(resolve, durationMsec));
			mediaRecorder.stop();
			// wait data
			await new Promise(resolve => {
				const tid = setInterval(() => {
					if (blob == null) return;
					clearInterval(tid);
					resolve();
				}, 10);
			});
			stream.getVideoTracks()[0].stop();
			return await blobToDataURL(blob);
		}

		function startDisplay(stream) {
			message("録画中･･･");
			outputArea.appendChild(info);
			outputArea.appendChild(video)
			video.srcObject = stream;
			video.play();
		}

		function stopDisplay() {
			video.pause();
			video.parentNode.removeChild(video);
			message("録画終了。転送処理中･･･");
		}

		// https://stackoverflow.com/questions/23150333
		async function blobToDataURL(blob) {
			return await new Promise((resolve, reject) => {
				const reader = new FileReader();
				reader.onload = () => resolve(reader.result);
				reader.onerror = () => reject(reader.error);
				reader.onabort = () => reject(new Error("Read aborted"));
				reader.readAsDataURL(blob);
			});
		}

		function message(str) {
			info.textContent = str;
		}

		function clearInfo() {
			info.parentNode.removeChild(info);
		}
	"""

	try:
		display(Javascript(_js))
		data = eval_js(f"""record({duration}, {frame_rate}, {wh[0]}, {wh[1]})""")
		bin = b64decode(data.split("base64,")[1])
		eval_js("""message("動画準備中･･･")""")
		ffmpeg.input("pipe:").output(out_file).overwrite_output().run_async(pipe_stdin=True).communicate(input=bin)
		eval_js("clearInfo()")
		return True

	except Exception as err:
		print(f"Error: {str(err)}")
		return False

print("録画準備完了")
