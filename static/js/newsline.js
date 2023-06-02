let newslineList = []
$.ajax({
    url: 'http://127.0.0.1:8000/api/news/',
    method: 'GET',
    success: function(data, status) {
        for (let i = 0; i < data.length; i++) {
            newslineList.push(data[i]);
        }
    },
    error: function(response, status) {
    }
});
$.ajax({
    url: 'http://127.0.0.1:8000/api/events/',
    method: 'GET',
    success: function(data, status) {
        for (let i = 0; i < data.length; i++) {
            newslineList.push(data[i]);
        }
    },
    error: function(response, status) {
    }
});
//function newslineListSort(List) {
//    for (let i = 0; i < List.length; i++) {
//        for (let j = 0; j < List.length; j++) {
//            if (List[i].id > List[j].id) {
//                [List[i], List[j]] = [List[j], List[i]];
//            }
//        }
//    }
//    return List
//}
const newsline = document.getElementById('newsline');
for (let i = 0; i < newslineList.length ; i++) {
    console.log(1)
    const newsBlock = document.createElement('div');
    const newsName = document.createElement('p');
    newsName.innerText = newslineList[i].name
    newsBlock.append(newsName)
    newsline.append(newsBlock)
    const newsNameLink = document.createElement('a');
    const newsCities = document.createElement('p');
    const newsDescription = document.createElement('p');
    if (newslineList[i].photo.length > 1 ){
        for (let i = 0; i < newslineList[i].photo.length; i++){
            const newsPhoto = document.createElement('img');
        }
    } else {
        const newsPhoto = document.createElement('img');
    }
};