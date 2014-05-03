
% Twitch Plays Pokemon, Machine Learns Twitch
% Author: Albert Haque
% Date: May 2014

% This file generates anomaly scores using k-means clustering. Each point
% is compared to the centroid and a distance is calculated. This distance
% is used as the anomaly score.

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

% Use k-means clustering, k=1, and find distance of each point to prototype
ANOMALY_THRESHOLD = 40;
[IDX,C, sumd, distances] = kmeans(featureMatrix,1);
numUsers = length(distanceMatrix);
kmeans_scores = normalizeToAnomalyScore(distances');
numTrolls = 0;
troll_users = [];
for i = 1:numUsers
    if kmeans_scores(i) > ANOMALY_THRESHOLD
        numTrolls = numTrolls + 1;
        troll_users = [troll_users; featureMatrix(i,:)];
    end
end

averageFeatureDistance = mean(troll_users(:,:)) - C;
bar(averageFeatureDistance);
xlabel('Feature Number');
ylabel('Average Distance from Prototype');

% SVD
%{
meanCentered = featureMatrix - mean(featureMatrix(:));
[U,S,V] = svd(meanCentered);
scatter(-U(:,1), -U(:,2), 'xk');
%}

%{
hist(kmeans_scores, 100);
grid;
xlabel('Anomaly Score');
ylabel('Number of Points with Score');
%}

% Used to generate anomaly score distributions

%{
[n4, xout4] = hist(sknn_scores1, 100);
b4 = bar(xout4,n4,'k');
grid;
hold on;

[n3, xout3] = hist(sknn_scores5, 100);
b3 = bar(xout3,n3,'b');

[n2, xout2] = hist(sknn_scores50, 100);
b2 = bar(xout2,n2,'g');

[n1, xout1] = hist(sknn_scores500, 100);
b1 = bar(xout1,n1,'r');

ah1 = gca;
ah2 = axes('position',get(gca,'position'), 'visible','off');
ah3 = axes('position',get(gca,'position'), 'visible','off');
ah4 = axes('position',get(gca,'position'), 'visible','off');
legend(ah1, b1, 'Location', [0.7 0.85 0.15 0.05], 'k=500')
legend(ah2, b2, 'Location', [0.7 0.75 0.15 0.05], 'k=50')
legend(ah3, b3, 'Location', [0.7 0.65 0.15 0.05], 'k=5')
legend(ah4, b4, 'Location', [0.7 0.55 0.15 0.05], 'k=1')
hold off
toc
%}