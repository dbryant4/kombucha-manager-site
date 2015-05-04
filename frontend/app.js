(function(){
	var app = angular.module('kombucha_manager', []);

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

	app.controller('BatchController', function(){
		this.batches = batches.results;

		this.getBatches = function(){
			return this.batches;
		};
		
	});

	app.controller('BottleController', function(){
		
	});

	app.controller('VesselController', function(){
		
	});

	var batches = {
	    "count": 1,
	    "next": null,
	    "previous": null,
	    "results": [
	        {
	        	"id": 1,
	            "tea": [
	                "https://kombucha-manager.herokuapp.com/api/v1/teas/3/"
	            ],
	            "tea_volume": "5.0",
	            "sugar_volume": "1.00",
	            "brew_volume": "1.00",
	            "scoby_count": 2,
	            "brew_date": "2015-04-22",
	            "comments": "",
	            "vessel": [
	                "https://kombucha-manager.herokuapp.com/api/v1/vessels/1/"
	            ]
	        }
	    ]
	}

	var tea_types = [
		{
			name: 'Green',
		},
		{
			name: 'White',
		},
		{
			name: 'Black',
		}
	];
})();
