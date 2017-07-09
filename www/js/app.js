'use strict'

angular.module('meagram', ['ngRoute'])
    .config(['$routeProvider',
            function($routeProvider) {
                $routeProvider
                    .when('/', {
                        templateUrl: 'html/main.html',
                        controller: 'MainController'
                    })
                    .otherwise({
                        redirectTo: '/'
                    });
            }])
    .controller('MainController', ['$scope', '$http', 
            function($scope, $http) {

            }])
    .controller('HeaderController', ['$scope', '$http',
            function($scope, $http) {
                var header = this;
                $http.get('/subscribes').then(function(response){
                    var subs = response.data;
                    header.subscribes = subs;
                });
            }])
    .controller('LoginController', ['$scope', '$http',
            function($scope, $http) {
                this.success = true;
            }]);
