(function(){
	var app = angular.module('bottles', []);
	
	app.directive('addBottleForm', function(){
		return {
			restrict: 'E',
			templateUrl: '/static/add-bottle-form.html'
		};
	});

	app.controller('BottleController', ['$filter', '$http', '$log', '$scope', function($filter, $http, $log, $scope){
		$scope.loadBottles = function(url){
			url = url || "/api/v1/bottles/";
			$scope.bottleLoader = $http.get(url)
			.success(function(response) {
				bottles = response.results;
	    		
	    		bottles.forEach(function(bottle){
	    			$scope.bottleLoader = $http.get(bottle.size)
	    			.success(function(response){	
	    				bottle.size = response;
	    			})
	    		});
	    		$scope.bottles = $scope.bottles.concat(bottles);
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
					bottle_date: $filter('date')($scope.newBottle.bottle_date, 'yyyy-MM-dd'),
					size: $scope.newBottle.size,
					batch: $scope.newBottle.batch,
				},
			}
			$scope.bottleLoader = $http(req)
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