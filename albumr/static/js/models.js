function l(string) {
    console.log(string);
}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var base_url = 'http://127.0.0.1:8000/';

pageModel = function (page) {
    var self = this;

    self.page_name = ko.observable(page.name);
    self.page_id = ko.observable(page.id);
    self.position = ko.observable(page.position);
    self.template = ko.observable(page.template);

    /* Page Has Multiple Items */
    self.items = ko.observableArray(
        ko.utils.arrayMap(page.items, function (item) {
            return new itemModel(item, page.items.length);
        })
    );
    if (page.items.length < 3) {
        for (var i = page.items.length; i < 3; i++) {
            var item = new itemModel(null, i);
            self.items.push(item);
        }
    }

}

itemModel = function (item, len) {
    var self = this;
    if (!item) {
        item = [];
        item.id = '';
        item, image_url = '';
        item.position = len;
    }
    self.item_id = ko.observable(item.id);
    self.image_url = ko.observable(item.image_url);
    self.position = ko.observable(item.position);
}

createViewModel = function () {
    var viewModel = {
        pages:ko.observableArray([]),
        allLayouts:ko.observableArray([ 'template1', 'template2', 'template3']),

        chosenPageId:ko.observable(),
        chosenItemId:ko.observable(),

        chosenPage:ko.observable(),
        chosenItem:ko.observable(),

        selectedPage:ko.observable()
    };

    viewModel.loadPages = function () {
        var album_id = $('.album_id').val();
        if(isNaN(location.hash))
            window.location.hash = '';

        $.ajax({
            url:base_url + 'albums/get/' + album_id,
            dataType:'json',
            beforeSend:function (xhr) {
            },
            success:function (data) {
                viewModel.pages.removeAll();
                $.each(data.pages, function (index, item) {
                    var obj = new pageModel(item)
                    viewModel.pages.push(obj);
                });

                if (viewModel.pages().length > 0) {
                    // initialize the page
                    var pid = location.hash.replace('#', '');
                    var current_page = ko.utils.arrayFilter(viewModel.pages(), function (item) {
                        return item.page_id() == pid;
                    });

                    if (current_page.length > 0) {
                        viewModel.chosenPage(current_page[0]);
                        viewModel.chosenPageId(pid);

                        if (current_page[0].items().length > 0) {
                            viewModel.chosenItem(current_page[0].items()[0]);
                        }
                    }
                    else {
                        viewModel.chosenPage(viewModel.pages()[0]);
                        viewModel.chosenPageId(viewModel.pages()[0].page_id());

                        if (viewModel.pages()[0].items().length > 0) {
                            viewModel.chosenItem(viewModel.pages()[0].items()[0]);
                        }

                    }
                }
            }
        });
    };

    viewModel.currentPages = ko.computed(function() {
        return  ko.utils.arrayFilter(viewModel.pages(), function (item) {
            return !item._destroy
        });
    });

    viewModel.addPage = function () {

        var obj = new Object();
        var len = viewModel.currentPages().length + 1;
        obj.id = 'n' + len;
        obj.position = len - 1;
        obj.name = 'New Page' + len;
        obj.template = viewModel.allLayouts()[0];
        obj.items = [
            {'position':0, 'image_url':''},
            {'position':1, 'image_url': ''},
            {'position':2, 'image_url': ''}
        ];

        var p = new pageModel(obj);
        viewModel.pages.push(p);
        location.hash = 'n' + len;
    };

    viewModel.deletePage = function(page) {
        // destroy page
        viewModel.pages.destroy(page);

        if(viewModel.currentPages().length > 0) {
            $.each(viewModel.currentPages(), function (index, item) {
                item.position(index);
            });
            window.location.hash = ko.toJS(viewModel.currentPages()[0]['page_id']);
        }else {
            viewModel.chosenPage(false);
            viewModel.chosenItem(false);
            window.location.hash = '';
        }
    };

    viewModel.goToPage = function (p) {
        location.hash = ko.toJS(p).page_id;
    };

    viewModel.selectItem = function (item) {
        viewModel.chosenItem(item);
    };

    viewModel.isPageSelected = function (page) {
        return page == viewModel.chosenPage();
    };

    viewModel.isItemSelected = function (item) {
        return item == viewModel.chosenItem();
    };

    viewModel.save = function () {
        var pages = ko.toJS(viewModel.pages());
        $.ajax(base_url + "albums/save_all/", {
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            data:{
                json:ko.toJSON({
                    pages:pages,
                    album_id:$(".album_id").val()
                })
            },
            type:"POST",
            dataType:'json',
            beforeSend:function () {

            },
            success:function (result) {
               // l(result);
                if(result.pages) {
                    window.location.hash = result.pages[0]['id'];
                    location.reload();
                }
            },
            error: function(x,y,z) {
                l(x);
            }
        });
    };


    viewModel.pageDropCallback = function (arg) {
        $.each(viewModel.currentPages(), function (index, item) {
            item.position(index);
        });

    };

    return viewModel;
}
