import FinanceDataReader as web
from datetime import date, timedelta
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import platform

#폰트 깨짐 방식
from matplotlib import font_manager, rc
if platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
elif platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
else:
    pass

today = date.today()
startday = date.today() - timedelta(720)
yesterday = date.today() - timedelta(1)
print(yesterday)

SEC = web.DataReader("KS11", startday, yesterday) #finance 라이브러리 사용
print(type(SEC))
print(SEC.tail(10)) # 끝 10개 만 프린트
# SEC['Close'].plot(figsize=(16,4))

plt.subplot(311) #차트를 3행 1열 (첫번째)
plt.title("KOSPI Chart")
plt.ylim([2000, 3500])     # Y축의 범위: [ymin, ymax], 가격범위
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d'))

SEC[startday:yesterday]['Close'].plot(figsize=(16,10), style='b',xlabel='Date', ylabel='종가')
plt.subplots_adjust(hspace=0.5)

SEC = web.DataReader("USD/KRW", startday, yesterday) #finance 라이브러리 사용
print(type(SEC))
print(SEC.tail(10)) # 끝 10개 만 프린트
# SEC['Close'].plot(figsize=(16,4))

plt.subplot(312)
plt.title("USD/KRW Currency Chart")
plt.ylim([1000, 2000])     # Y축의 범위: [ymin, ymax], 가격범위
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d'))

SEC[startday:yesterday]['Close'].plot(figsize=(16,10), style='b',xlabel='Date', ylabel='종가')
plt.subplots_adjust(hspace=0.5)

SEC = web.DataReader("BTC/KRW", startday, yesterday) #finance 라이브러리 사용
print(type(SEC))
print(SEC.tail(10)) # 끝 10개 만 프린트
# SEC['Close'].plot(figsize=(16,4))

plt.subplot(313)
plt.title("BTC/KRW Chart")
plt.ylim([20000000, 80000000])     # Y축의 범위: [ymin, ymax], 가격범위
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d'))

SEC[startday:yesterday]['Close'].plot(figsize=(16,10), style='b',xlabel='Date', ylabel='종가')
plt.subplots_adjust(hspace=0.5)

plt.show()