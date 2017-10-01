/* minifyOnSave, filenamePattern: $1.min.$2 */
(function($) {

	$.fn.paginate = function(options) {
		//Options
		var settings = $.extend({
			pageLength: 20,
			nbPages: 0,
			headerSelector: "thead",
			bodySelector: "tbody",
			rowSelector: "tr",
			footerSelector: "tfoot",
			paginationButtonsClass: "",
			paginationButtonsTagName: "button",
			paginationButtonsContainerClass: "",
			previousButtonContent: "&lt;",
			nextButtonContent: "&gt;",
			previousButtonId: "", //Ids des boutons
			nextButtonId: "",
		}, options);

		//Vérifications des options
		if ( !(/^[a-z]+$/i.test(settings.paginationButtonsTagName)) )
			throw "error in JQuery.paginemytable: paginationButtonsTagName must contain only letters. Characters [" + settings.paginationButtonsTagName.match(/[^a-z]/gi).join(", ") + "] found";

		if ( !(/^[a-z]+$/i.test(settings.headerSelector)) )
			throw "error in JQuery.paginemytable: headerSelector must contain only letters. Characters [" + settings.headerSelector.match(/[^a-z]/gi).join(", ") + "] found";

		if ( !(/^[a-z]+$/i.test(settings.bodySelector)) )
			throw "error in JQuery.paginemytable: bodySelector must contain only letters. Characters [" + settings.bodySelector.match(/[^a-z]/gi).join(", ") + "] found";

		if ( !(/^[a-z]+$/i.test(settings.rowSelector)) )
			throw "error in JQuery.paginemytable: rowSelector must contain only letters. Characters [" + settings.rowSelector.match(/[^a-z]/gi).join(", ") + "] found";

		if ( !(/^[a-z]+$/i.test(settings.footerSelector)) )
			throw "error in JQuery.paginemytable: footerSelector must contain only letters. Characters [" + settings.footerSelector.match(/[^a-z]/gi).join(", ") + "] found";


		if ( settings.pageLength === 0 )
			throw "error in JQuery.paginemytable: pageLength can not be 0";

		if ( settings.pageLength == 1 )
			console.warn("Be careful, using paginemytable with pageLength = 1 is most likely to create unreadable tables");


		//Fonctions
		var switchTablePage = function(table, n) {
			var next = parseInt(settings.nbPages+1);
			var previous = 0;
			var table_index = table.data("index");


			if ( n < previous || n > next)
				return;

			if ( (table_index == 1 && n == previous) || (n == next && table_index == parseInt(settings.nbPages)) )
				return;

			switch (n) {
				case previous:
					switchTablePage(table, parseInt(table.data("index")) - 1);
					break;

				case next:
					switchTablePage(table, parseInt(table.data("index")) + 1);
					break;

				default:
					console.log(table.data("index") + " => " + n);
					table.find("tbody").css("display", "none");
					table.find("tbody:nth-of-type(" + n + ")").css("display", "table-row-group");
					table.data("index", parseInt(n));
			}
		};

		var initTableBody = function(table) {
			var rows = table.find(settings.bodySelector + " " + settings.rowSelector);
			var tableBody = table.find(settings.bodySelector);

			settings.nbPages = ( settings.nbPages > rows.length / settings.pageLength || settings.nbPages === 0 ) ? rows.length / settings.pageLength : settings.nbPages; //Pour ne pas générer plus de pages qu'il n'en faut
			settings.nbPages = Math.ceil(settings.nbPages);

			//On vide la table, son contenu étant stocké dans rows
			tableBody.remove();

			//Séparation du corps en plusieurs tbody
			for ( var i = 0 ; i < settings.nbPages ; i++ ) //Ensuite, pour chaque pages, on découpe un tbody
			{
				table.append("<tbody></tbody>");

				for ( var j = i*settings.pageLength ; j < (i+1)*settings.pageLength && j < rows.length ; j++ ) { //Et on ajoute les éléments qui vont bien sur chaque tbody
					table.find("tbody").last().append(rows[j]);
				}
			}
			table.find("tbody:not(:first-of-type)").css("display", "none"); //On cache tout sauf la première page
			table.data("index", 1); //Et on met l'index à 1
		};

		var initTableFooter = function(table) {
			var nbColumns = table.find(settings.headerSelector + " tr").children().length;
			var tableFoot = table.find(settings.footerSelector);

			//Maintenant on prépare le footer pour la pagination
			tableFoot.empty(); //On s'assure que le footer est vide
			tableFoot.append("<tr><td colspan='" + nbColumns + "'></td></tr>");
			var pagination = tableFoot.find("tr td");
			pagination.addClass(settings.paginationButtonsContainerClass);

			//On prépare la pagination < 1 2 3 4 5 6 ... >
			if ( settings.previousButtonContent )
				pagination.append("<" + settings.paginationButtonsTagName + " type='button' class='pagination previous " + settings.paginationButtonsClass + "' id='" + settings.previousButtonId + "'>" + settings.previousButtonContent + "</" + settings.paginationButtonsTagName + ">");

			for ( var i = 0 ; i < settings.nbPages ; i++ ) {
				pagination.append("<" + settings.paginationButtonsTagName + " type='button' class='pagination " + settings.paginationButtonsClass + "'> " + (i+1) + " </" + settings.paginationButtonsTagName + ">");
			}

			if ( settings.nextButtonContent )
				pagination.append("<" + settings.paginationButtonsTagName + " type='button' class='pagination next " + settings.paginationButtonsClass + "' id='" + settings.nextButtonId + "'>" + settings.nextButtonContent + "</" + settings.paginationButtonsTagName + ">");

			//Callback sur les boutons de pagination
			pagination.find(settings.paginationButtonsTagName).each(function(i) { //On met les callbacks sur les spans
				$(this).click(function(){
					switchTablePage(table, i);
				});
			});
		};

		var initTable = function(table) {
			initTableBody(table);
			initTableFooter(table);
		};
		//Fin des fonctions

		//Main
		this.each(function(index) {
			initTable($(this));
		});

		return this;

	}; // Fin de paginate()
}(jQuery));


// my-pagination any class use
$(document).ready(function() {
	$(".my-pagination").paginate({
					paginationButtonsClass: "button",
					paginationButtonsContainerClass: "pagination-button",
					previousButtonContent: "<i class='fa fa-angle-double-left' aria-hidden='true'></i>",
					nextButtonContent: "<i class='fa fa-angle-double-right' aria-hidden='true'></i>",
					pageLength: 20,
				});
		});
