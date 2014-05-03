
% Twitch Plays Pokemon, Machine Learns Twitch
% Author: Albert Haque
% Date: May 2014

% This file generates anomaly scores using distance to the sum of the 
% k nearest neighbor and plots the percent of users labeled as a troll

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

fprintf('Calculating SKNN k=500\n');
sknn_scores500 = SKNN(500, distanceMatrix);
fprintf('Calculating SKNN k=50\n');
sknn_scores50 = SKNN(50, distanceMatrix);
fprintf('Calculating SKNN k=5\n');
sknn_scores5 = SKNN(5, distanceMatrix);
fprintf('Calculating SKNN k=1\n')
sknn_scores1 = SKNN(1, distanceMatrix);
fprintf('Done calculating SKNN\n');

fprintf('Calculating how many trolls...\n');
ANOMALY_THRESHOLD = 40;
numUsers = length(sknn_scores1);
numberTrolls = zeros(1,4);

for i = 1:numUsers
    if sknn_scores1(1,i) > ANOMALY_THRESHOLD
        numberTrolls(1) = numberTrolls(1) + 1;
    end
    if sknn_scores5(1,i) > ANOMALY_THRESHOLD
        numberTrolls(2) = numberTrolls(2) + 1;
    end
    if sknn_scores50(1,i) > ANOMALY_THRESHOLD
        numberTrolls(3) = numberTrolls(3) + 1;
    end
    if sknn_scores500(1,i) > ANOMALY_THRESHOLD
        numberTrolls(4) = numberTrolls(4) + 1;
    end
end
fprintf('Done!\n');

numberTrolls = numberTrolls/numUsers;
bar(numberTrolls');
legend('SKNN','Location','NorthWest');
grid;
set(gca, 'YTickMode','auto');
set(gca, 'YTickLabel',num2str(100.*get(gca,'YTick')','%g%%'));
set(gca,'XTickLabel',{'k=1', 'k=5', 'k=50', 'k=500'});

