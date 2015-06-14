(function(){
	var app = angular.module('kombucha_manager', ['angular-loading-bar', 'smart-table'])
	.config(['cfpLoadingBarProvider', function(cfpLoadingBarProvider) {
    	cfpLoadingBarProvider.includeSpinner = false;
  	}]);

	app.directive('loginForm', function(){
		return {
			restrict: 'E',
			templateUrl: '/static/login-form.html'
		};
	});
	app.directive('addBatchForm', function(){
		return {
			restrict: 'E',
			templateUrl: '/static/add-batch-form.html'
		};
	});
	app.directive('batchPanel', function(){
		return {
			restrict: 'E',
			templateUrl: '/static/batch-panel.html'
		};
	});
	app.directive('bottlePanel', function(){
		return {
			restrict: 'E',
			templateUrl: '/static/bottle-panel.html'
		};
	});
	app.directive('vesselPanel', function(){
		return {
			restrict: 'E',
			templateUrl: '/static/vessel-panel.html'
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

	app.controller('BatchController', ['$scope', '$http', '$log', function($scope, $http, $log){
		$scope.loadBatches = function(url){
			url = url || "/api/v1/batches/";
			$http.get(url)
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
	    		$scope.batches = $scope.batches.concat(batches);
	    		if (response.next != null){
						$scope.loadBatches(response.next);
				}
	    	})
	    	.error(function(response, status, headers, config) {
	    		if (status == 403) {
	    			$('#loginModal').on('shown.bs.modal', function () {
	  					$('#username').focus()
					})
	    			$('#loginModal').modal('show');
	    		}
	    	});
    	};

		this.addBatch = function(){
			$log.debug($scope);
		};

		$scope.batches = [];
		$scope.loadBatches();
	} ]);

	app.controller('BottleController', ['$http', '$log', '$scope', function($http, $log, $scope){
		$scope.loadBottles = function(url){
			url = url || "/api/v1/bottles/";
			$http.get(url)
			.success(function(response) {
	    		$scope.bottles = $scope.bottles.concat(response.results);
	    		if (response.next != null){
					$scope.loadBottles(response.next);
				}
	    	})
	    	.error(function(response, status, headers, config) {
	    		if (status == 403) {
	    			$('#loginModal').on('shown.bs.modal', function () {
	  					$('#username').focus()
					})
	    			$('#loginModal').modal('show');
	    		}
	    	});
    	};
    	
    	$scope.bottles = [];
    	$scope.loadBottles();
	} ]);

	app.controller('VesselController', ['$http', '$log', '$scope', function($http, $log, $scope){
		$scope.loadVessels = function(url){
			url = url || "/api/v1/vessels/";
			$scope.vessels = [];
			$http.get(url)
			.success(function(response) {
				$scope.vessels = $scope.vessels.concat(response.results);
				if (response.next != null){
					loadVessels(response.next);
				}
	    	})
	    	.error(function(response, status, headers, config) {
	    		if (status == 403) {
	    			$('#loginModal').on('shown.bs.modal', function () {
	  					$('#username').focus()
					})
	    			$('#loginModal').modal('show');
	    		}
	    	});
		};
		$scope.vessels = [];
		$scope.loadVessels();
	} ]);

	app.controller('TeaController', ['$http', '$log', '$scope', function($http, $log, $scope){
		this.loadTeas = function(url){
			url = url || "/api/v1/teas/";
			$http.get(url)
			.success(function(response) {
	    		$scope.teas = response['results'];
	    	})
	    	.error(function(response, status, headers, config) {
	    		if (status == 403) {
	    			$('#loginModal').on('shown.bs.modal', function () {
	  					$('#username').focus()
					})
	    			$('#loginModal').modal('show');
	    		}
	    	});

			this.joinNames = function(objects){
				var return_str = "";

				angular.forEach(objects, function(object){
					return_str = return_str + object.name + ' ';
				});

				return return_str;
			};
		};

		this.loadTeas();
	} ]);
	
})();