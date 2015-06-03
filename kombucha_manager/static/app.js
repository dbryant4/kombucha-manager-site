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
	
	app.controller('loginController', ['$scope' , '$http', '$log', function($scope, $http, $log){
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
				$log.debug(data.key)
				$('#loginModal').modal('hide');
  			}).
  			error(function(data, status, headers, config) {
  				$('#username').addClass("has-error");
  				$('#password').addClass("has-error");
			});
		};

		this.logout = function() {
			var req = {
			 	method: 'POST',
			 	url: '/api/v1/rest-auth/logout/',
			 	headers: {
			   		'Content-Type': 'application/json'
			 	},
			}
			$http(req).
			success(function(data, status, headers, config) {
				$http.defaults.headers.common.Authorization = undefined;	
				
  			}).
  			error(function(data, status, headers, config) {
				$http.defaults.headers.common.Authorization = undefined;
				
			});
		};
	} ]);

	app.controller('ManagerController', function(){
		this.tea_types = tea_types;
	});

	app.controller('PanelController', function(){
		this.tab = 'batches'; // Default tab

		this.selectTab = function(setTab){
			this.tab = setTab;
		};

		this.isSelected = function(checkTab){
			return this.tab === checkTab;
		};
	});

	app.controller('BatchController', ['$http', '$log', function($http, $log){
		var batches = this;

		$http.get("/api/v1/batches/")
		.success(function(response) {
    		batches = response['results'];
    		for (x in batches){
    			/* Get tea objects 
    			for (t in batches[x]['tea']){
    				$http.get(batches[x]['tea'][t])
    				.success(function(response){					
    					batches[x]['tea'][t] = response;
    				});
    			}*/
    			$log.debug(batches[x]['vessel']);
    			/* Get vessel objects 
    			$http.get(batches[x]['vessel'])
    			.success(function(response){	
    				$log.debug(response);

    				batches[x]['vessel'] = response;
    			})*/
    		};
    		$log.debug(batches);
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

		this.getTea = function(id){
			var req = {
			 	method: 'GET',
			 	url: '/api/v1/teas/' + id + '/',
			 	headers: {
			   		'Content-Type': 'application/json'
			 	},
			}
			$http(req)
			.success(function(data, status, headers, config) {
				return data;
  			})
  			.error(function(data, status, headers, config) {
  				return data;
			});
		};
	} ]);

	var tea_types = [
        {
            "id": 1,
            "name": "Green",
            "url": "http://127.0.0.1:8000/api/v1/teatypes/1/"
        },
        {
            "id": 2,
            "name": "Black",
            "url": "http://127.0.0.1:8000/api/v1/teatypes/2/"
        },
        {
            "id": 3,
            "name": "White",
            "url": "http://127.0.0.1:8000/api/v1/teatypes/3/"
        }
    ]; 
})();