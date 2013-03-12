$(".pages")                .attr("data-bind", "sortable:  {data: pages, afterMove: $root.pageDropCallback, options: { containment: 'parent' }}");
$(".plist")                .attr('data-bind', "text: ( parseInt(position()) +1 ), click: $root.goToPage");
$(".plist").parent()       .attr('data-bind', 'css: {selectedp: $root.isPageSelected($data)}')


$(".page_options")          .attr('data-bind', 'with: chosenPage, visible: $root.currentPages().length > 0');
$(".page_options").parent()          .attr('data-bind', 'visible: $root.currentPages().length > 0');
$(".nopage")                .attr('data-bind', 'visible: $root.currentPages().length == 0');

$(".pname")                 .attr('data-bind', 'value: page_name');
$(".ptemplate")             .attr("data-bind", "options: $root.allLayouts(), value: template");


$(".item_options")          .attr('data-bind', 'with: chosenItem');
$(".image_url")             .attr('data-bind', 'value: image_url');

// Editor
$(".page-editor")           .attr('data-bind', 'with: chosenPage, visible: $root.currentPages().length > 0');
$('.template')               .attr('data-bind',"attr: { class: 'template ' + template()  } ");

$('.items_list')             .attr('data-bind', 'foreach: items');

$('.items')                  .attr('data-bind', 'attr: {class : "items item" + position() }, click: $root.selectItem, '
                                + ' css: {selectedi: $root.isItemSelected($data)}');

$('.item_img')              .attr('data-bind', 'attr: {src: image_url}');


// Actions
$(".add_page")			    .attr('data-bind', 'click: addPage');
$("#save_all")              .attr('data-bind', 'click: save');
$(".delpage")                .attr('data-bind', 'click: $root.deletePage');




vm = createViewModel();

ko.applyBindings(vm);

if(typeof(loadpages) != 'undefined' && loadpages) {
    setTimeout(function() {
        vm.loadPages();
    }, 20);
}

// Handle Routing -Client-side routes
Sammy(
    function () {
        var s = this;
        this.get('#:page_id', function () {
            var page_id = this.params.page_id;
            var current_page = ko.utils.arrayFilter(vm.pages(), function (page) {
                return page.page_id() == page_id;
            });

            // if page exists
            if (current_page.length > 0) {
                vm.chosenPageId(page_id);
                vm.chosenPage(current_page[0]);

                vm.chosenItem(current_page[0].items()[0]);
                vm.chosenItemId(current_page[0].items()[0].item_id());

                l(ko.toJS(vm));
                l('SAMMY CALLED');
            }
            else {
                s.get('/');
            }
        });
    }).run();

