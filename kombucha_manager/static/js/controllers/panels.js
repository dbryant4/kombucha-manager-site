(function(){
	var app = angular.module('panels', []);
	app.directive('batchPanel', function(){
		return {
			restrict: 'E',
			templateUrl: '/static/batch-panel.html'
		};
	});
	app.directive('vesselPanel', function(){
		return {
			restrict: 'E',
			templateUrl: '/static/vessel-panel.html'
		};
	});
	app.directive('bottlePanel', function(){
		return {
			restrict: 'E',
			templateUrl: '/static/bottle-panel.html'
		};
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

})();