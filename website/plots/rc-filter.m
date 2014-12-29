A = csvread('../spice/rc-filter-2.csv');
h = semilogx(A(:,1), A(:,2))
xlabel('Frequency (Hz)')
ylabel('Amplitude (dB)')
title('RC Filter Output')
grid on;
print('../static/images/plots/rc-filter.svg', '-dsvg')
pause
