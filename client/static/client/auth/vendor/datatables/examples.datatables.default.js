(function($) {
	'use strict';
	var datatableInit = function() {
		$('#datatable-default').dataTable({
			dom: '<"row"<"col-lg-6"l><"col-lg-6"f>><"table-responsive"t>p',
			"pageLength": 25,
			"lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]]
		});

		$('#news-table').dataTable({
			dom: '<"row"<"col-lg-6"l><"col-lg-6"f>><"table-responsive"t>p',
			"pageLength": 100,
			"lengthMenu": [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]]
		});
	};
	$(function() {
		datatableInit();
	});
}).apply(this, [jQuery]);