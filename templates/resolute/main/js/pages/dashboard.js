//[Dashboard Javascript]

//Project:	Qixa Admin - Responsive Admin Template
//Primary use:   Used only for the main dashboard (index.html)


$(function () {

  'use strict';
	
// Counter
	
		$('.countnm').each(function () {
			$(this).prop('Counter',0).animate({
				Counter: $(this).text()
			}, {
				duration: 5000,
				easing: 'swing',
				step: function (now) {
					$(this).text(Math.ceil(now));
				}
			});
		});
	// donut chart
		$('.donut').peity('donut');
		
		// bar chart
		$(".bar").peity("bar");	
	
	// Morris-chart
	
	Morris.Area({
        element: 'morris-area-chart2',
        data: [{
            period: '2012',
            SiteA: 485,
            SiteB: 358,
            
        }, {
            period: '2013',
            SiteA: 359,
            SiteB: 210,
            
        }, {
            period: '2014',
            SiteA: 589,
            SiteB: 410,
            
        }, {
            period: '2015',
            SiteA: 458,
            SiteB: 344,
            
        }, {
            period: '2016',
            SiteA: 254,
            SiteB: 200,
            
        }, {
            period: '2017',
            SiteA: 754,
            SiteB: 630,
            
        },
         {
            period: '2018',
            SiteA: 845,
            SiteB: 711,
           
        }],
        xkey: 'period',
        ykeys: ['SiteA', 'SiteB'],
        labels: ['Total Ticket', 'Close Ticket'],
        pointSize: 5,
        fillOpacity: 0.8,
        pointStrokeColors:['#fb8d34', '#5e2572'],
        behaveLikeLine: true,
        gridLineColor: '#e0e0e0',
        lineWidth: 3,
        smooth: true,
        hideHover: 'auto',
        lineColors: ['#fb8d34', '#5e2572'],
        resize: true
        
    });
	
	//BAR CHART
    var bar = new Morris.Bar({
      element: 'bar-chart',
      resize: true,
      data: [
        {y: 'Mon', a: 4, b: 5, c: 6},
        {y: 'Tue', a: 1, b: 2, c: 3},
        {y: 'Wed', a: 7, b: 5, c: 3},
        {y: 'Thu', a: 1, b: 2, c: 5},
        {y: 'Fri', a: 9, b: 5, c: 9},
        {y: 'Sat', a: 10, b: 5, c: 6},
		{y: 'Sun', a: 5, b: 3, c: 7}
      ],
		barColors: ['#5e2572', '#7c3196', '#9b33bf'],
		barSizeRatio: 0.5,
		barGap:5,
		xkey: 'y',
		ykeys: ['a', 'b', 'c'],
		labels: ['Morning', 'Evening', 'Night'],
		hideHover: 'auto'
    });
	
	//sparkline
		$("#barchart4").sparkline([32,24,26,24,32,26,40,34,22,24], {
			type: 'bar',
			height: '120',
			width: '65%',
			barWidth: 8,
			barSpacing: 4,
			barColor: '#ffffff',
		});
		$("#linearea3").sparkline([32,24,26,24,32,26,40,34,22,24], {
			type: 'line',
			width: '50%',
			height: '120',
			lineColor: '#ffffff',
			fillColor: '#ffffff',
			lineWidth: 1,
		});
	
		



}); // End of use strict

