```matlab
clc;
clear;
load matlab.mat;

x = [1 3 5 7 9 11 13 15];
new_x = [2 4 6 8 10 12 14 16];
p = zeros(size(X, 1), numel(new_x));

for i = 1:size(X, 1)
    p(i, :) = spline(x, X(i, :), new_x);
    figure(i);
    plot(x, X(i, :), 'o', new_x, p(i, :), 'r-');
    legend('样本点','三次样条插值','Location','SouthEast')
end

```


