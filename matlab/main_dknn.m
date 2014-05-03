
% Twitch Plays Pokemon, Machine Learns Twitch
% Author: Albert Haque
% Date: May 2014

% This file generates anomaly scores using distance to the k nearest
% neighbor and plots the percent of users labeled as a troll

set(0,'DefaultAxesFontSize', 12);
set(0,'DefaultTextFontSize', 12);

% This code takes roughly 1-3 minutes to run.
rawMatrix = csvread('full_features-active.csv');
featureMatrix = rawMatrix(:,2:end);

fprintf('Calculating Distance Matrix...\n');
tic
distanceMatrix = calculateDistanceMatrix(featureMatrix);
toc
fprintf('Done!\n');


fprintf('Calculating DKNN k=500\n');
dknn_scores500 = DKNN(500, distanceMatrix);
fprintf('Calculating DKNN k=50\n');
dknn_scores50 = DKNN(50, distanceMatrix);
fprintf('Calculating DKNN k=5\n');
dknn_scores5 = DKNN(5, distanceMatrix);
fprintf('Calculating DKNN k=1\n')
dknn_scores1 = DKNN(1, distanceMatrix);
fprintf('Done calculating KNN\n');

fprintf('Calculating how many trolls...\n');
ANOMALY_THRESHOLD = 40;
numUsers = length(dknn_scores1);
numberTrolls = zeros(1,4);

for i = 1:numUsers
    if dknn_scores1(1,i) > ANOMALY_THRESHOLD
        numberTrolls(1) = numberTrolls(1) + 1;
    end
    if dknn_scores5(1,i) > ANOMALY_THRESHOLD
        numberTrolls(2) = numberTrolls(2) + 1;
    end
    if dknn_scores50(1,i) > ANOMALY_THRESHOLD
        numberTrolls(3) = numberTrolls(3) + 1;
    end
    if dknn_scores500(1,i) > ANOMALY_THRESHOLD
        numberTrolls(4) = numberTrolls(4) + 1;
    end
end
fprintf('Done!\n');

numberTrolls = numberTrolls/numUsers;
bar(numberTrolls');
legend('DKNN','Location','NorthWest');
grid;
set(gca, 'YTickMode','auto');
set(gca, 'YTickLabel',num2str(100.*get(gca,'YTick')','%g%%'));
set(gca,'XTickLabel',{'k=1', 'k=5', 'k=50', 'k=500'});

