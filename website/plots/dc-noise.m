dc = 9 + zeros(100,1);
noise = rand(100,1)/10 - rand(100,1)/10;
hold on
plot(dc+noise);
plot(dc, 'r');
ylim([8.75 9.25])
print('../static/images/plots/dc-noise.svg', '-dsvg')
pause

