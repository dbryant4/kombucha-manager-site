(function(){
	var app = angular.module('batches', []);
	app.directive('addBatchForm', function(){
		return {
			restrict: 'E',
			templateUrl: '/static/add-batch-form.html'
		};
	});

	app.controller('BatchController', ['$filter', '$scope', '$http', '$window', '$log', function($filter, $scope, $http, $window, $log){
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
			$http(req).
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

		$scope.discardBatch = function(id){
			var req = {
			 	method: 'POST',
			 	url: '/api/v1/batches/' + id + '/discard/',
			 	headers: {
			   		'Content-Type': 'application/json'
			 	},
			}
			$http(req).
			success(function(data, status, headers, config) {
				$log.debug(data);
  			}).
  			error(function(data, status, headers, config) {
  				$window.alert("Error " + status + " while saving " + field + ". Your changes were NOT saved.");
  				$log.debug(data)
  				$log.debug(status)
			});
		};

		$scope.patchBatch = function(url, field, value){
			data = {};
			data[field] = value;
			var req = {
			 	method: 'PATCH',
			 	url: url,
			 	headers: {
			   		'Content-Type': 'application/json'
			 	},
			 	data: data,
			}
			$http(req).
			success(function(data, status, headers, config) {
				$log.debug(data);
  			}).
  			error(function(data, status, headers, config) {
  				$window.alert("Error " + status + " while saving " + field + ". Your changes were NOT saved.");
  				$log.debug(data)
  				$log.debug(status)
  			});
		};

		$scope.newBatch = {};
		$scope.batches = [];
		$scope.loadBatches();
	} ]);
})();