(function(){
	var app = angular.module('kombucha_manager', ['angular-loading-bar'])
	.config(['cfpLoadingBarProvider', function(cfpLoadingBarProvider) {
    	cfpLoadingBarProvider.includeSpinner = false;
  	}]);

	app.directive('loginForm', function(){
		return {
			restrict: 'E',
			templateUrl: 'login-form.html'
		};
	});
	app.directive('addBatchForm', function(){
		return {
			restrict: 'E',
			templateUrl: 'add-batch-form.html'
		};
	});
	app.directive('batchTable', function(){
		return {
			restrict: 'E',
			templateUrl: 'batch-table.html'
		};
	});
	app.directive('bottleTable', function(){
		return {
			restrict: 'E',
			templateUrl: 'bottle-table.html'
		};
	});
	app.directive('vesselTable', function(){
		return {
			restrict: 'E',
			templateUrl: 'vessel-table.html'
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

	
	app.controller('PanelController', function(){
		this.tab = 'batches'; // Default tab

		this.selectTab = function(setTab){
			this.tab = setTab;
		};

		this.isSelected = function(checkTab){
			return this.tab === checkTab;
		};
	});

	app.controller('BatchController', ['$scope', '$http', '$log', '$rootScope', function($scope, $http, $log, $rootScope){
		var batches = this; 

		$http.get("/api/v1/batches/")
		.success(function(response) {

    		batches = response['results'];
    		batches.forEach(function(batch){
    			/* Get tea objects*/
    			var new_teas = [];
    			batch['tea'].forEach(function(tea){

					$http.get(tea)
    				.success(function(response){					
    					new_teas.push(response);
    				});
    			});
    			batch['tea'] = new_teas;

    			/* Get vessel objects */
    			$http.get(batch['vessel'])
    			.success(function(response){	
    				batch['vessel'] = response;
    			})

    		});
    	})
    	.error(function(response, status, headers, config) {
    		if (status == 403) {
    			$('#loginModal').on('shown.bs.modal', function () {
  					$('#username').focus()
				})
    			$('#loginModal').modal('show');
    		}
    	});

		this.getBatches = function(){
			return batches;
		};

		this.addBatch = function(){
			$log.debug($scope);
		};
	} ]);

	app.controller('BottleController', ['$http', '$log', function($http, $log){
		var bottles = this;

		$http.get("/api/v1/bottles/")
		.success(function(response) {
    		bottles = response['results'];
    	})
    	.error(function(response, status, headers, config) {
    		if (status == 403) {
    			$('#loginModal').on('shown.bs.modal', function () {
  					$('#username').focus()
				})
    			$('#loginModal').modal('show');
    		}
    	});

		this.getBottles = function(){
			return bottles;
		};
	} ]);

	app.controller('VesselController', ['$http', '$log', function($http, $log){
		var vessels = this;

		$http.get("/api/v1/vessels/")
		.success(function(response) {
    		vessels = response['results'];
    		
    	})
    	.error(function(response, status, headers, config) {
    		if (status == 403) {
    			$('#loginModal').on('shown.bs.modal', function () {
  					$('#username').focus()
				})
    			$('#loginModal').modal('show');
    		}
    	});

		this.getVessels = function(){
			return vessels;
		};
	} ]);

	app.controller('TeaController', ['$http', '$log', function($http, $log){
		var teas = this;

		$http.get("/api/v1/teas/")
		.success(function(response) {
    		teas = response['results'];
    		
    	})
    	.error(function(response, status, headers, config) {
    		if (status == 403) {
    			$('#loginModal').on('shown.bs.modal', function () {
  					$('#username').focus()
				})
    			$('#loginModal').modal('show');
    		}
    	});

		this.getTeas = function(){
			return teas;
		};

		this.joinNames = function(objects){
			var return_str = "";

			angular.forEach(objects, function(object){
				return_str = return_str + object.name + ' ';
			});

			return return_str;
		};
	} ]);

	var token = undefined;

	
})();