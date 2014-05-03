% Author: Albert Haque
% Date: April 2014
% Twitch Plays Pokemon, Machine Learns Twitch

% This function calculates the Euclidean distance between two high
% dimensional points

function [ distance ] = euclideanDistance(p1, p2)
    distance = sqrt(sum((p1-p2).^2));
end