(function(){
	var app = angular.module('authentication', []);
	app.directive('loginForm', function(){
		return {
			restrict: 'E',
			templateUrl: '/static/login-form.html'
		};
	});
	
	app.controller('loginController', ['$scope' , '$http', '$window', '$log', function($scope, $http, $window, $log){
		$scope.login = function() {
			var req = {
			 	method: 'POST',
			 	url: '/api/v1/rest-auth/login/',
			 	headers: {
			   		'Content-Type': 'application/json'
			 	},
			 	data: {
			 		username:$scope.username,
				  	password:$scope.password
				},
			}
			$http(req).
			success(function(data, status, headers, config) {
				$http.defaults.headers.common.Authorization = 'Token ' + data.key;
				$('#loginModal').modal('hide');
				$window.location.reload();	
  			}).
  			error(function(data, status, headers, config) {
  				$('#username').addClass("has-error");
  				$('#password').addClass("has-error");
			});
		};

		this.logout = function() {
			var req = {
			 	method: 'GET',
			 	url: '/api/v1/auth/logout/?next=/',
			 	headers: {
			   		'Content-Type': 'application/json'
			 	},
			}
			$http(req).
			success(function(data, status, headers, config) {
				$http.defaults.headers.common.Authorization = undefined;	
				$window.location.reload();
  			}).
  			error(function(data, status, headers, config) {
				$http.defaults.headers.common.Authorization = undefined;
				
			});
		};
	} ]);
})();