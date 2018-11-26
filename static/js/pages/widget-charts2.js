//[widget charts Javascript]

//Project:	Unique Admin - Responsive Admin Template
//Primary use:   Used only for the  widget charts



$( document ).ready(function() {
    "use strict";
	
	if( $('#chart_1').length > 0 ){
		var ctx1 = document.getElementById("chart_1").getContext("2d");
		var data1 = {
			labels: ["January", "February", "March", "April", "May", "June", "July"],
			datasets: [
			{
				label: "fir",
				backgroundColor: "#5e2572",
				borderColor: "#5e2572",
				pointBorderColor: "#5e2572",
				pointHighlightStroke: "#5e2572",
				data: [0, 59, 40, 75, 50, 45, 80]
			},
			{
				label: "sec",
				backgroundColor: "#7c3196",
				borderColor: "#7c3196",
				pointBorderColor: "#7c3196",
				pointBackgroundColor: "#7c3196",
				data: [48, 88, 50, 58, 34, 67, 65],
			}
			
		]
		};
		
		var areaChart = new Chart(ctx1, {
			type:"line",
			data:data1,
			
			options: {
				tooltips: {
					mode:"label"
				},
				elements:{
					point: {
						hitRadius:90
					}
				},
				
				scales: {
					yAxes: [{
						stacked: true,
						gridLines: {
							color: "rgba(135,135,135,0)",
						},
						ticks: {
							fontFamily: "Poppins",
							fontColor:"#878787"
						}
					}],
					xAxes: [{
						stacked: true,
						gridLines: {
							color: "rgba(135,135,135,0)",
						},
						ticks: {
							fontFamily: "Poppins",
							fontColor:"#878787"
						}
					}]
				},
				animation: {
					duration:	3000
				},
				responsive: true,
				legend: {
					display: false,
				},
				tooltip: {
					backgroundColor:'rgba(33,33,33,1)',
					cornerRadius:0,
					footerFontFamily:"'Poppins'"
				}
				
			}
		});
	}
    
	if( $('#chart_2').length > 0 ){
		var ctx2 = document.getElementById("chart_2").getContext("2d");
		var data2 = {
			labels: ["January", "February", "March", "April", "May", "June", "July"],
			datasets: [
				{
					label: "My First dataset",
					backgroundColor: "#5e2572",
					borderColor: "#5e2572",
					data: [10, 59, 40, 75, 50, 45, 80]
				},
				{
					label: "My Second dataset",
					backgroundColor: "#7c3196",
					borderColor: "#7c3196",
					data: [48, 88, 50, 58, 34, 67, 65]
				}
			]
		};
		
		var hBar = new Chart(ctx2, {
			type:"horizontalBar",
			data:data2,
			
			options: {
				tooltips: {
					mode:"label"
				},
				scales: {
					yAxes: [{
						stacked: true,
						gridLines: {
							color: "rgba(135,135,135,0)",
						},
						ticks: {
							fontFamily: "Poppins",
							fontColor:"#878787"
						}
					}],
					xAxes: [{
						stacked: true,
						gridLines: {
							color: "rgba(135,135,135,0)",
						},
						ticks: {
							fontFamily: "Poppins",
							fontColor:"#878787"
						}
					}],
					
				},
				elements:{
					point: {
						hitRadius:40
					}
				},
				animation: {
					duration:	3000
				},
				responsive: true,
				legend: {
					display: false,
				},
				tooltip: {
					backgroundColor:'rgba(33,33,33,1)',
					cornerRadius:0,
					footerFontFamily:"'Poppins'"
				}
				
			}
		});
	}

	if( $('#chart_3').length > 0 ){
		var ctx3 = document.getElementById("chart_3").getContext("2d");
		var data3 = {
			labels: ["Eating", "Drinking", "Sleeping", "Designing", "Coding", "Cycling", "Running"],
			datasets: [
				{
					label: "My First dataset",
					backgroundColor: "rgba(94, 37, 114, 0.6)",
					borderColor: "rgba(94, 37, 114, 0.6)",
					pointBackgroundColor: "rgba(94, 37, 114, 0.6)",
					pointBorderColor: "#fff",
					pointHoverBackgroundColor: "#fff",
					pointHoverBorderColor: "rgba(94, 37, 114, 0.6)",
					data: [65, 59, 90, 81, 56, 55, 40]
				},
				{
					label: "My Second dataset",
					backgroundColor: "rgba(155, 51, 191, 1)",
					borderColor: "rgba(155, 51, 191, 1)",
					pointBackgroundColor: "rgba(155, 51, 191, 1)",
					pointBorderColor: "#fff",
					pointHoverBackgroundColor: "#fff",
					pointHoverBorderColor: "rgba(155, 51, 191, 1)",
					data: [28, 48, 40, 19, 96, 27, 100]
				}
			]
		};
		var radarChart = new Chart(ctx3, {
			type: "radar",
			data: data3,
			options: {
					scale: {
						ticks: {
							beginAtZero: true,
							fontFamily: "Poppins",
							
						},
						gridLines: {
							color: "rgba(135,135,135,0)",
						},
						pointLabels:{
							fontFamily: "Poppins",
							fontColor:"#878787"
						},
					},
					
					animation: {
						duration:	3000
					},
					responsive: true,
					legend: {
							labels: {
							fontFamily: "Poppins",
							fontColor:"#878787"
							}
						},
						elements: {
							arc: {
								borderWidth: 0
							}
						},
						tooltip: {
						backgroundColor:'rgba(33,33,33,1)',
						cornerRadius:0,
						footerFontFamily:"'Poppins'"
					}
			}
		});
	}

	if( $('#chart_4').length > 0 ){
		var ctx4 = document.getElementById("chart_4").getContext("2d");
		var data4 = {
			datasets: [{
				data: [
					11,
					16,
					7,
					3,
					14
				],
				backgroundColor: [
					"#4b1a5c",
					"#5e2572",
					"#7c3196",
					"#9b33bf",
					"#c248ec"
				],
				hoverBackgroundColor: [
					"#4b1a5c",
					"#5e2572",
					"#7c3196",
					"#9b33bf",
					"#c248ec"
				],
				label: 'My dataset' // for legend
			}],
			labels: [
				"lab 1",
				"lab 2",
				"lab 3",
				"lab 4",
				"lab 5"
			]
		};
		var polarChart = new Chart(ctx4, {
			type: "polarArea",
			data: data4,
			options: {
				elements: {
					arc: {
						borderColor: "#fff",
						borderWidth: 0
					}
				},
				scale: {
					ticks: {
						beginAtZero: true,
						fontFamily: "Poppins",
						
					},
					gridLines: {
						color: "rgba(135,135,135,0)",
					}
				},
				animation: {
					duration:	3000
				},
				responsive: true,
				legend: {
					labels: {
					fontFamily: "Poppins",
					fontColor:"#878787"
					}
				},
				tooltip: {
					backgroundColor:'rgba(33,33,33,1)',
					cornerRadius:0,
					footerFontFamily:"'Poppins'"
				}
			}
		});
	}

	if( $('#chart_5').length > 0 ){
		var ctx5 = document.getElementById("chart_5").getContext("2d");
		var data5 = {
			datasets: [
				{
					label: 'First Dataset',
					data: [
						{
							x: 80,
							y: 60,
							r: 10
						},
						{
							x: 40,
							y: 40,
							r: 10
						},
						{
							x: 30,
							y: 40,
							r: 20
						},
						{
							x: 20,
							y: 10,
							r: 10
						},
						{
							x: 50,
							y: 30,
							r: 10
						}
					],
					backgroundColor:"#5e2572",
					hoverBackgroundColor: "#7c3196",
				},
				{
					label: 'Second Dataset',
					data: [
						{
							x: 40,
							y: 30,
							r: 10
						},
						{
							x: 25,
							y: 20,
							r: 10
						},
						{
							x: 35,
							y: 30,
							r: 10
						}
					],
					backgroundColor:"#9b33bf",
					hoverBackgroundColor: "#c248ec",
				}]
		};
		
		var bubbleChart = new Chart(ctx5,{
			type:"bubble",
			data:data5,
			options: {
				elements: {
					points: {
						borderWidth: 1,
						borderColor: 'rgb(33, 33, 33)'
					}
				},
				scales: {
					xAxes: [
					{
						ticks: {
							min: -10,
							max: 100,
							fontFamily: "Poppins",
							fontColor:"#878787"
						},
						gridLines: {
							color: "rgba(135,135,135,0)",
						}
					}],
					yAxes: [
					{
						ticks: {
							fontFamily: "Poppins",
							fontColor:"#878787"
						},
						gridLines: {
							color: "rgba(135,135,135,0)",
						}
					}]
				},
				animation: {
					duration:	3000
				},
				responsive: true,
				legend: {
					labels: {
					fontFamily: "Poppins",
					fontColor:"#878787"
					}
				},
				tooltip: {
					backgroundColor:'rgba(33,33,33,1)',
					cornerRadius:0,
					footerFontFamily:"'Poppins'"
				}
			}
		});
	}

	if( $('#chart_6').length > 0 ){
		var ctx6 = document.getElementById("chart_6").getContext("2d");
		var data6 = {
			 labels: [
			"lab 1",
			"lab 2",
			"lab 3"
		],
		datasets: [
			{
				data: [300, 50, 100],
				backgroundColor: [
					"#5e2572",
					"#7c3196",
					"#9b33bf"
				],
				hoverBackgroundColor: [
					"#5e2572",
					"#7c3196",
					"#9b33bf"
				]
			}]
		};
		
		var pieChart  = new Chart(ctx6,{
			type: 'pie',
			data: data6,
			options: {
				animation: {
					duration:	3000
				},
				responsive: true,
				legend: {
					labels: {
					fontFamily: "Poppins",
					fontColor:"#878787"
					}
				},
				tooltip: {
					backgroundColor:'rgba(33,33,33,1)',
					cornerRadius:0,
					footerFontFamily:"'Poppins'"
				},
				elements: {
					arc: {
						borderWidth: 0
					}
				}
			}
		});
	}

	if( $('#chart_7').length > 0 ){
		var ctx7 = document.getElementById("chart_7").getContext("2d");
		var data7 = {
			 labels: [
			"lab 1",
			"lab 2",
			"lab 3"
		],
		datasets: [
			{
				data: [300, 50, 100],
				backgroundColor: [
					"#5e2572",
					"#7c3196",
					"#9b33bf"
				],
				hoverBackgroundColor: [
					"#5e2572",
					"#7c3196",
					"#9b33bf"
				]
			}]
		};
		
		var doughnutChart = new Chart(ctx7, {
			type: 'doughnut',
			data: data7,
			options: {
				animation: {
					duration:	3000
				},
				responsive: true,
				legend: {
					labels: {
					fontFamily: "Poppins",
					fontColor:"#878787"
					}
				},
				tooltip: {
					backgroundColor:'rgba(33,33,33,1)',
					cornerRadius:0,
					footerFontFamily:"'Poppins'"
				},
				elements: {
					arc: {
						borderWidth: 0
					}
				}
			}
		});
	}
	
	if( $('#chart_8').length > 0 ){
		var ctx2 = document.getElementById("chart_8").getContext("2d");
		var data2 = {
			labels: ["January", "February", "March", "April", "May", "June", "July"],
			datasets: [
				{
					label: "My First dataset",
					backgroundColor: "#310d3d",
					borderColor: "#310d3d",
					data: [15, 20, 70, 51, 36, 85, 50]
				},
				{
					label: "My Second dataset",
					backgroundColor: "#5e2572",
					borderColor: "#5e2572",
					data: [28, 48, 40, 19, 86, 27, 90]
				},
				{
					label: "My Third dataset",
					backgroundColor: "#9b33bf",
					borderColor: "#9b33bf",
					data: [8, 28, 50, 29, 76, 77, 40]
				}
			]
		};
		
		var hBar = new Chart(ctx2, {
			type:"bar",
			data:data2,
			
			options: {
				tooltips: {
					mode:"label"
				},
				scales: {
					yAxes: [{
						stacked: true,
						gridLines: {
							color: "rgba(135,135,135,0)",
						},
						ticks: {
							fontFamily: "Poppins",
							fontColor:"#878787"
						}
					}],
					xAxes: [{
						stacked: true,
						gridLines: {
							color: "rgba(135,135,135,0)",
						},
						ticks: {
							fontFamily: "Poppins",
							fontColor:"#878787"
						}
					}],
					
				},
				elements:{
					point: {
						hitRadius:40
					}
				},
				animation: {
					duration:	3000
				},
				responsive: true,
				maintainAspectRatio:false,
				legend: {
					display: false,
				},
				
				tooltip: {
					backgroundColor:'rgba(33,33,33,1)',
					cornerRadius:0,
					footerFontFamily:"'Poppins'"
				}
				
			}
		});
	}
	
}); // End of use strict
