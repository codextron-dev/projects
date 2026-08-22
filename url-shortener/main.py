import pyshorteners

s = pyshorteners.Shortener()
short_url = s.tinyurl.short("https://www.anthropic.com/research/reviewing-the-evidence-on-worker-retraining-programs")
print(short_url)