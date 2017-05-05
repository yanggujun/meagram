'use strict'

angular.module('meagram', ['ngRoute'])
    .config(['$routeProvider',
            function($routeProvider) {
                $routeProvider
                    .when('/', {
                        templateUrl: 'main.html',
                        controller: 'MainController'
                    })
                    .otherwise({
                        redirectTo: '/'
                    });
            }])
    .controller('MainController', ['$scope', '$http', 
            function($scope, $http) {

            }]);
