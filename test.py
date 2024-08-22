import azure.cognitiveservices.speech as speechsdk
import speech_recognition as sr
import os

# 初始化语音合成配置
speech_config = speechsdk.SpeechConfig(subscription="AZURE密钥", region="地区")
speech_config.speech_synthesis_voice_name = 'zh-CN-XiaoxiaoNeural'
audio_output_format = speechsdk.SpeechSynthesisOutputFormat.Riff16Khz16BitMonoPcm
speech_config.set_speech_synthesis_output_format(audio_output_format)
speech_config.speech_recognition_language = "zh-CN"  # 设置为中文

# 文件夹路径
input_folder = r'C:\Users\shilo\Desktop\ipod\test\input'
output_folder = r'C:\Users\shilo\Desktop\ipod\test\output'

# 遍历文件夹中的所有 WAV 文件
for filename in os.listdir(input_folder):
    if filename.endswith(".wav"):
        input_file_path = os.path.join(input_folder, filename)

        # 创建音频配置并识别
        audio_input = speechsdk.audio.AudioConfig(filename=input_file_path)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

        result = speech_recognizer.recognize_once()
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            text = result.text
            print(f"识别的文本: {text}")

            # 使用 Azure 语音合成将文本转换回音频文件并保存
            output_file_path = os.path.join(output_folder, filename)
            audio_config = speechsdk.audio.AudioOutputConfig(filename=output_file_path)
            speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

            speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

            if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                print(f"语音合成成功，并保存为 [{output_file_path}]，文本为: [{text}]")
            elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = speech_synthesis_result.cancellation_details
                print("语音合成取消: {}".format(cancellation_details.reason))
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    if cancellation_details.error_details:
                        print("错误详情: {}".format(cancellation_details.error_details))
                        print("请检查语音服务的密钥和区域值是否设置正确。")

print("处理完成。")



# # 初始化识别器
# recognizer = sr.Recognizer()
#
# # 遍历文件夹中的所有 WAV 文件
# for filename in os.listdir(input_folder):
#     if filename.endswith(".wav"):
#         input_file_path = os.path.join(input_folder, filename)
#
#         # 加载音频文件
#         with sr.AudioFile(input_file_path) as source:
#             audio = recognizer.record(source)  # 读取整个音频文件
#
#         try:
#             # 使用 Google Web Speech API 进行语音识别
#             text = recognizer.recognize_google(audio, language="zh-CN")
#             print(f"识别的文本: {text}")
#
#             # 使用 Azure 语音合成将文本转换回音频文件并保存
#             output_file_path = os.path.join(output_folder, filename)
#             audio_config = speechsdk.audio.AudioOutputConfig(filename=output_file_path)
#             speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
#
#             speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
#
#             if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
#                 print(f"语音合成成功，并保存为 [{output_file_path}]，文本为: [{text}]")
#             elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
#                 cancellation_details = speech_synthesis_result.cancellation_details
#                 print("语音合成取消: {}".format(cancellation_details.reason))
#                 if cancellation_details.reason == speechsdk.CancellationReason.Error:
#                     if cancellation_details.error_details:
#                         print("错误详情: {}".format(cancellation_details.error_details))
#                         print("请检查语音服务的密钥和区域值是否设置正确。")
#         except sr.UnknownValueError:
#             print(f"无法识别音频中的语音，文件: {filename}")
#         except sr.RequestError as e:
#             print(f"语音识别服务错误; {e}")
#
# print("处理完成。")