function l(string) {
    console.log(string);
}

pageModel = function (page) {
    var self = this;

    self.page_name = ko.observable(page.name);
    self.page_id = ko.observable(page.id);
    self.position = ko.observable(page.position);
    self.template = ko.observable(page.template);

    /* Page Has Multiple Items */
    self.items = ko.observableArray(
        ko.utils.arrayMap(page.items, function (item) {
            return new itemModel(item);
        })
    );
}

itemModel = function(item) {

    var self = this;
    self.item_id = ko.observable(item.id);
    self.image_url = ko.observable(item.image_url);
    self.position = ko.observable(item.position);
}

createViewModel = function() {
    var viewModel = {
        pages:ko.observableArray([]),
        allLayouts: ko.observableArray([ 'template1', 'template2']),

        chosenPageId:ko.observable(),
        chosenItemId:ko.observable(),

        chosenPage:ko.observable(),
        chosenItem:ko.observable(),

        selectedPage:ko.observable()
    };


    viewModel.loadPages = function () {
        viewModel.pages.removeAll();

        var obj = {'name': 'first page', 'template':'template2', 'position':0, 'id':1,
            'items': [{'image_url':'google', 'position':0}, {'image_url': 'flickr', 'position':1}]
            }   ;
        var p = new pageModel(obj);
        viewModel.pages.push(p);

        // initialize the page
        var pid = location.hash.replace('#','');

        var current_page = ko.utils.arrayFilter(viewModel.pages(), function (item) {
            return item.page_id() == pid;
        });

        if(current_page.length > 0 ) {
            viewModel.chosenPage(current_page[0]);
            viewModel.chosenPageId(pid);
            viewModel.chosenItem(current_page[0].items()[0]);

        }
        else {
            viewModel.chosenPage(viewModel.pages()[0]);
            viewModel.chosenPageId(viewModel.pages()[0].page_id());
            viewModel.chosenItem(viewModel.pages()[0].items()[0]);

        }

    };

    viewModel.addPage = function () {

        var obj = new Object();
        var len = viewModel.pages().length + 1;
        obj.id = 'n' + len;
        obj.position = len -1;
        obj.name = 'New Page' + len;
        obj.template = 'template1';
        obj.items = [{'position':0, 'image_url': ''}, {'position':1, 'image_url': ''}, {'position':2, 'image_url': ''}];

        var p = new pageModel(obj);
        viewModel.pages.push(p);
        location.hash = 'n' + len;
    };

    viewModel.goToPage = function(p) {
        location.hash = ko.toJS(p).page_id;
    };

    viewModel.selectItem = function(item) {
        viewModel.chosenItem(item);
    };

    viewModel.isPageSelected = function(page) {
        return page == viewModel.chosenPage();
    };

    viewModel.isItemSelected = function(item) {
        return item == viewModel.chosenItem();
    };
    viewModel.save = function() {

    }

    viewModel.pageDropCallback = function (arg) {
        $.each(viewModel.pages(), function (index, item) {
            item.position(index);
        });

    };

    return viewModel;
}
