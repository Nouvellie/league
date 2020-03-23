var app = angular.module('leagueStats', []);
app.config(function ($interpolateProvider) {
    'use strict';
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});
app.controller("leagueStatsController", function ($scope) {
    'use strict';
    $scope.searchSummoner = function ($event) {
        $event.preventDefault();
        var data = {
            nick: $scope.summonerName
        };
        console.log(data);
    };
});