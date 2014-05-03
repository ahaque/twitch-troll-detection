
% Twitch Plays Pokemon, Machine Learns Twitch
% Author: Albert Haque
% Date: May 2014

% This function takes distances and normalizes them to [0,100]

function [ anomalyScores ] = normalizeToAnomalyScore( rawScores )
% Input: array of scores
% Output: array of scores scaled so min=0 and max=100
    adjusted = rawScores - ones(1, length(rawScores))*min(rawScores);
    scaleFactor = 100/max(adjusted);
    anomalyScores = adjusted*scaleFactor;
end

