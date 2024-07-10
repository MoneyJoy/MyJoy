### code2

```matlab
%% 灰色关联分析用于综合评价模型例题的讲解
clear;clc
load data_water_quality.mat
% 不会导入数据的同学可以看看第二讲topsis模型，我们也可以自己在工作区新建变量，并把Excel的数据粘贴过来
% 注意Matlab的当前文件夹一定要切换到有数据文件的这个文件夹内

%%  判断是否需要正向化
[n,m] = size(X);
disp(['共有' num2str(n) '个评价对象, ' num2str(m) '个评价指标']) 
Judge = input(['这' num2str(m) '个指标是否需要经过正向化处理，需要请输入1 ，不需要输入0：  ']);   %1

if Judge == 1
    Position = input('请输入需要正向化处理的指标所在的列，例如第2、3、6三列需要处理，那么你需要输入[2,3,6]： '); %[2,3,4]
    disp('请输入需要处理的这些列的指  标类型（1：极小型， 2：中间型， 3：区间型） ')
    Type = input('例如：第2列是极小型，第3列是区间型，第6列是中间型，就输入[1,3,2]：  '); %[2,1,3]
    % 注意，Position和Type是两个同维度的行向量
    for i = 1 : size(Position,2)  %这里需要对这些列分别处理，因此我们需要知道一共要处理的次数，即循环的次数
        X(:,Position(i)) = Positivization(X(:,Position(i)),Type(i),Position(i));
    % Positivization是我们自己定义的函数，其作用是进行正向化，其一共接收三个参数
    % 第一个参数是要正向化处理的那一列向量 X(:,Position(i))   回顾上一讲的知识，X(:,n)表示取第n列的全部元素
    % 第二个参数是对应的这一列的指标类型（1：极小型， 2：中间型， 3：区间型）
    % 第三个参数是告诉函数我们正在处理的是原始矩阵中的哪一列
    % 该函数有一个返回值，它返回正向化之后的指标，我们可以将其直接赋值给我们原始要处理的那一列向量
    end
    disp('正向化后的矩阵 X =  ')
    disp(X)
end

%% 对正向化后的矩阵进行预处理
Mean = mean(X);  % 求出每一列的均值以供后续的数据预处理
Z = X ./ repmat(Mean,size(X,1),1);  
disp('预处理后的矩阵为：'); disp(Z)

%% 构造母序列和子序列
Y = max(Z,[],2);  % 母序列为虚拟的，用每一行的最大值构成的列向量表示母序列
X = Z; % 子序列就是预处理后的数据矩阵

%% 计算得分
absX0_Xi = abs(X - repmat(Y,1,size(X,2)))  % 计算|X0-Xi|矩阵
a = min(min(absX0_Xi))    % 计算两级最小差a
b = max(max(absX0_Xi))  % 计算两级最大差b
rho = 0.5; % 分辨系数取0.5
gamma = (a+rho*b) ./ (absX0_Xi  + rho*b)  % 计算子序列中各个指标与母序列的关联系数
weight = mean(gamma) / sum(mean(gamma));  % 利用子序列中各个指标的灰色关联度计算权重
score = sum(X .* repmat(weight,size(X,1),1),2);   % 未归一化的得分
stand_S = score / sum(score);   % 归一化后的得分
[sorted_S,index] = sort(stand_S ,'descend') % 进行排序
```

### Inter2Max

```matlab
function [posit_x] = Inter2Max(x,a,b)
    r_x = size(x,1);  % row of x 
    M = max([a-min(x),max(x)-b]);
    posit_x = zeros(r_x,1);   %zeros函数用法: zeros(3)  zeros(3,1)  ones(3)
    % 初始化posit_x全为0  初始化的目的是节省处理时间
    for i = 1: r_x
        if x(i) < a
           posit_x(i) = 1-(a-x(i))/M;
        elseif x(i) > b
           posit_x(i) = 1-(x(i)-b)/M;
        else
           posit_x(i) = 1;
        end
    end
end
```

### Mid2Max

```matlab
function [posit_x] = Mid2Max(x,best)
    M = max(abs(x-best));
    posit_x = 1 - abs(x-best) / M;
end
```

### Min2Max

```matlab
function [posit_x] = Min2Max(x)
    posit_x = max(x) - x;
     %posit_x = 1 ./ x;    %如果x全部都大于0，也可以这样正向化
end
```

### Positivization

```matlab
function [posit_x] = Positivization(x,type,i)
% 输入变量有三个：
% x：需要正向化处理的指标对应的原始列向量
% type： 指标的类型（1：极小型， 2：中间型， 3：区间型）
% i: 正在处理的是原始矩阵中的哪一列
% 输出变量posit_x表示：正向化后的列向量
    if type == 1  %极小型
        disp(['第' num2str(i) '列是极小型，正在正向化'] )
        posit_x = Min2Max(x);  %调用Min2Max函数来正向化
        disp(['第' num2str(i) '列极小型正向化处理完成'] )
        disp('~~~~~~~~~~~~~~~~~~~~分界线~~~~~~~~~~~~~~~~~~~~')
    elseif type == 2  %中间型
        disp(['第' num2str(i) '列是中间型'] )
        best = input('请输入最佳的那一个值： ');
        posit_x = Mid2Max(x,best);
        disp(['第' num2str(i) '列中间型正向化处理完成'] )
        disp('~~~~~~~~~~~~~~~~~~~~分界线~~~~~~~~~~~~~~~~~~~~')
    elseif type == 3  %区间型
        disp(['第' num2str(i) '列是区间型'] )
        a = input('请输入区间的下界： ');
        b = input('请输入区间的上界： '); 
        posit_x = Inter2Max(x,a,b);
        disp(['第' num2str(i) '列区间型正向化处理完成'] )
        disp('~~~~~~~~~~~~~~~~~~~~分界线~~~~~~~~~~~~~~~~~~~~')
    else
        disp('没有这种类型的指标，请检查Type向量中是否有除了1、2、3之外的其他值')
    end
end
```


