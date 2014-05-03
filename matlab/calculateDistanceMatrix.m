% Author: Albert Haque
% Date: April 2014
% Twitch Plays Pokemon, Machine Learns Twitch

function [ distanceMatrix ] = calculateDistanceMatrix( featureMatrix )
% Input: featureMatrix = rows of feature vectors
% Output: distanceMatrix for each point to each other point

numUsers = length(featureMatrix);

% Calculate the distance matrix
distanceMatrix = NaN(numUsers, numUsers);
tic
for i = 1:numUsers
    for j = 1:numUsers
        if i == j
            distanceMatrix(i,j) = 0;
        elseif isnan(distanceMatrix(i,j))
            distance = sqrt(sum((featureMatrix(i,:)-featureMatrix(j,:)).^2));
            distanceMatrix(i,j) = distance;
            distanceMatrix(j,i) = distance;
        end % if
    end % j
    if mod(i, 500) == 0
        fprintf('Finished: %i / 9000\n', i);
        toc
    end
end % i