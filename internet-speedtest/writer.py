import pyautogui
import time

time.sleep(10)
inter = 0.2

pyautogui.write('import speedtest\n', interval = inter)
pyautogui.press("enter")

pyautogui.write('st = speedtest.Speedtest()\n', interval = inter)
pyautogui.press("enter")

pyautogui.write('download = st.download() / 1_000_000\n', interval = inter)

pyautogui.write('upload = st.upload() / 1_000_000\n', interval = inter)

pyautogui.write('ping = st.results.ping\n', interval = inter)
pyautogui.press("enter")

pyautogui.write('print(f"Download: {download:.2f} Mbps")\n', interval = inter)

pyautogui.write('print(f"Upload: {upload:.2f} Mbps")\n', interval = inter)

pyautogui.write('print(f"Ping: {ping:.2f} ms")\n', interval = inter)
