(function(){
	var app = angular.module('bottles', []);
	
	app.directive('addBottleForm', function(){
		return {
			restrict: 'E',
			templateUrl: '/static/add-bottle-form.html'
		};
	});

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

    	$scope.addBottle = function(){
			var req = {
			 	method: 'POST',
			 	url: '/api/v1/bottles/',
			 	headers: {
			   		'Content-Type': 'application/json'
			 	},
			 	data: {
					comment: "",
					flavors: [$scope.newBottle.flavor],
					bottle_date: $scope.newBottle.bottle_date,
					size: $scope.newBottle.size,
					batch: $scope.newBotttle.batch,
				},
			}
			$http(req)
			.success(function(data, status, headers, config) {
				$('#addBottleModal').modal('hide');
				$scope.bottles = [];
				$scope.loadBottles();
  			})
  			.error(function(data, status, headers, config) {
  				$log.debug(data);
			});
		};

    	$scope.newBottle = {};
    	$scope.bottles = [];
    	$scope.loadBottles();
	} ]);
})();