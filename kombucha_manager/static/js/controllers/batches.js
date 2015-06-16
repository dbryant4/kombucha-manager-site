(function(){
	var app = angular.module('batches', []);
	app.directive('addBatchForm', function(){
		return {
			restrict: 'E',
			templateUrl: '/static/add-batch-form.html'
		};
	});

	app.controller('BatchController', ['$filter', '$scope', '$http', '$log', function($filter, $scope, $http, $log){
		$scope.loadBatches = function(url){
			url = url || "/api/v1/batches/";
			$scope.batchLoader = $http.get(url)
			.success(function(response) {

	    		batches = response['results'];
	    		batches.forEach(function(batch){
	    			/* Get tea objects*/
	    			var new_teas = [];
	    			batch['tea'].forEach(function(tea){
						$scope.batchLoader = $http.get(tea)
	    				.success(function(response){					
	    					new_teas.push(response);
	    				});
	    			});
	    			batch['tea'] = new_teas;

	    			/* Get vessel objects */
	    			$scope.batchLoader = $http.get(batch['vessel'])
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

		$scope.addBatch = function(){
			var req = {
			 	method: 'POST',
			 	url: '/api/v1/batches/',
			 	headers: {
			   		'Content-Type': 'application/json'
			 	},
			 	data: {
					tea: [$scope.newBatch.tea],
				    tea_volume: $scope.newBatch.tea_volume,
				    sugar_volume: $scope.newBatch.sugar_volume,
				    brew_volume: $scope.newBatch.brew_volume,
				    scoby_count: $scope.newBatch.scoby_count,
				    brew_date: $filter('date')($scope.newBatch.brew_date, 'yyyy-MM-dd'),
				    comments: "",
				    vessel: $scope.newBatch.vessel
				},
			}
			$scope.batchLoader = $http(req).
			success(function(data, status, headers, config) {
				$log.debug(data);
				$('#addBatchModal').modal('hide');
				$scope.batches = [];
				$scope.loadBatches();
  			}).
  			error(function(data, status, headers, config) {
  				$log.debug(data);
			});
		};

		$scope.newBatch = {};
		$scope.batches = [];
		$scope.loadBatches();
	} ]);
})();