% 
figure()
A = csvread('../spice/rc-filter-1.csv');
plot(A(:,1), A(:,2))
xlabel('Frequency (Hz)')
ylabel('Amplitude (V/V)')
title('RC Filter Output')
pause

figure()
A = csvread('../spice/rc-filter-1.csv');
semilogx(A(:,1), A(:,2))
xlabel('Frequency (Hz)')
ylabel('Amplitude (V/V)')
title('RC Filter Output')
pause

figure()
A = csvread('../spice/rc-filter-2.csv');
plot(A(:,1), A(:,2))
xlabel('Frequency (Hz)')
ylabel('Amplitude (dB)')
title('RC Filter Output')
pause

figure()
A = csvread('../spice/rc-filter-2.csv');
semilogx(A(:,1), A(:,2))
xlabel('Frequency (Hz)')
ylabel('Amplitude (dB)')
title('RC Filter Output')
pause