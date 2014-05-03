
% Author: Albert Haque
% Date: April 2014
% Twitch Plays Pokemon, Machine Learns Twitch

% This function performs calculates distance based on the distance to the k
% nearest neighbor

function [ anomalyScores ] = DKNN( k, distanceMatrix)
% Input: k = kth nearest neighbor to compare to 
%        distanceMatrix = distance matrix (Euclidean distance)
% Output: list of anomaly scores. same order as row index in featureMatrix

numUsers = length(distanceMatrix);
% Find the distance to k nearest neighbor
knn_distances = NaN(1,numUsers);
for i = 1:numUsers
	sorted = sort(distanceMatrix(i,:));
    % Need to add 1 because there exists a 0 distance in the sorted list
    % (the distance of the point to itself)
    knn_distances(i) = sorted(k+1);
end

anomalyScores = normalizeToAnomalyScore(knn_distances);

end