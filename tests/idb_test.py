#!/usr/bin/python

import pytest
import sys

import parentpackage.classes.iDb as db


def test_db_fetch_reviews_table():
    #sql = "SELECT * FROM REVIEWS WHERE ISBN = 3622859490"
    #sql = "SELECT * FROM FAVORITES WHERE USER_ID = 12345"
    sql = "SELECT * FROM REVIEWS WHERE USER_ID = 12345"
    query_object = db.dbQuery(sql)
    results = db.dbQuery.callDbFetch(query_object)
    assert results == [{'USER_ID': 12345, 'RATING': 5, 'COMMENT': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc porta venenatis mattis. Integer lobortis velit nec tortor facilisis, eu malesuada lectus convallis. Suspendisse turpis lorem, cursus sed viverra sed, vestibulum vel ipsum. Maecenas sagittis justo sed facilisis pulvinar. Quisque semper rutrum mauris, et volutpat est tristique id. Sed vitae efficitur sapien. Phasellus non metus sed nisi vulputate malesuada. Nulla vitae elementum augue, tristique finibus turpis. Nam pharetra odio sed justo facilisis, non venenatis orci ultrices. Morbi non metus mollis, fringilla elit at, finibus urna. Fusce vitae urna ac sapien tincidunt bibendum vitae quis urna.', 'ISBN': '3622859490'}, {'USER_ID': 12345, 'RATING': 4, 'COMMENT': 'Pellentesque id ultricies neque, sit amet iaculis lorem. Suspendisse venenatis augue non tempor facilisis. Aenean auctor, metus sed maximus faucibus, massa dolor posuere nisi, in faucibus felis nibh convallis augue. Ut mollis erat eget sapien sodales, nec scelerisque erat euismod. Pellentesque aliquet, orci id dictum tristique, dolor est ultricies enim, vel ullamcorper nibh lorem a velit. Nullam facilisis posuere orci, eget condimentum quam accumsan sed. Vivamus sed nibh magna. Integer hendrerit neque eu nisi feugiat pretium. Vestibulum luctus libero ipsum, ac ornare arcu blandit non. Morbi finibus tristique turpis, eu aliquam dui vehicula et. Integer vel rutrum massa. Maecenas at ante id diam malesuada rutrum in ut neque. Nullam odio turpis, consequat eu eleifend quis, egestas quis magna. Etiam magna metus, convallis et lectus non, interdum sollicitudin purus.', 'ISBN': '1312041787'}, {'USER_ID': 12345, 'RATING': 3, 'COMMENT': 'In imperdiet ligula non rhoncus commodo. Maecenas et feugiat lorem, eget molestie dui. Nullam id metus quis enim consectetur accumsan finibus congue mauris. Donec vel enim et dolor consequat dictum. Proin at arcu et velit commodo accumsan. Fusce at interdum lacus, eget porttitor metus. Sed feugiat mollis nulla in accumsan. Donec mattis ex lacus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Vestibulum ut interdum massa. Phasellus porta neque velit, eu bibendum magna laoreet ac. Praesent ut magna vitae turpis interdum convallis.', 'ISBN': '8466284655'}, {'USER_ID': 12345, 'RATING': 2, 'COMMENT': 'Integer fringilla sit amet dui id vehicula. Curabitur sem nunc, mattis non lorem sed, rhoncus aliquam sapien. Donec a ultrices ante. Donec sit amet dui facilisis, cursus neque vitae, pulvinar tellus. Cras egestas libero arcu, ut accumsan arcu tempus eu. Vestibulum et dictum justo. Nullam nec libero nisl. Nunc sodales, purus eget eleifend egestas, sapien dui sagittis ligula, id lacinia urna neque eu libero. Vestibulum blandit ante at est ultricies finibus. Nunc ac risus imperdiet lacus efficitur dictum. Nullam viverra sagittis justo, hendrerit bibendum eros sollicitudin eget. Sed vel enim vitae mauris vulputate feugiat sit amet a mauris. Pellentesque id elit aliquet, iaculis ligula eget, iaculis metus. Duis pulvinar blandit lacus, egestas iaculis neque dignissim sit amet. Integer enim felis, rutrum at tempus nec, imperdiet a dolor. Aliquam erat volutpat.', 'ISBN': '5119609250'}, {'USER_ID': 12345, 'RATING': 1, 'COMMENT': 'Nunc sagittis vehicula placerat. Fusce vel congue massa. Proin sit amet mauris eu magna lacinia rhoncus vel sit amet ante. Suspendisse quis nulla vel est luctus interdum a sit amet sem. Quisque ullamcorper, leo non bibendum eleifend, dolor massa interdum arcu, ut tristique nulla magna in libero. Donec mollis luctus facilisis. Pellentesque fringilla faucibus justo ut maximus. Sed sed fermentum massa. Maecenas vitae enim quis mauris tempus blandit. Quisque rutrum et metus nec finibus. Morbi dignissim vulputate urna. Donec nisi lectus, gravida a mattis eget, posuere sed massa. Pellentesque urna dolor, lobortis sit amet est id, dictum egestas velit. Donec at bibendum purus, sit amet aliquam lorem. Sed ut lorem nibh. Ut eleifend, lacus non rhoncus tempus, nisi nisl pulvinar nulla, quis interdum nunc eros a lacus.', 'ISBN': '8676368961'}]

def test_db_fetch_favorites_table():
    #sql = "SELECT * FROM REVIEWS WHERE ISBN = '5930664514'"
    sql = "SELECT * FROM FAVORITES WHERE USER_ID = 12345"
    query_object = db.dbQuery(sql)
    results = db.dbQuery.callDbFetch(query_object)
    assert results == [{'USER_ID': '12345', 'ISBN': '1234567890'}, {'USER_ID': '12345', 'ISBN': '1234667890'}, {'USER_ID': '12345', 'ISBN': '1244667890'}]

def test_db_fetch_single_result():
    sql = "SELECT * FROM REVIEWS WHERE ISBN = '5930664514'"
    query_object = db.dbQuery(sql)
    results = db.dbQuery.callDbFetch(query_object)
    assert results == [{'USER_ID': 54321, 'RATING': 5, 'COMMENT': 'Donec hendrerit convallis est at consequat. Aliquam pretium, nulla non aliquet interdum, tellus augue accumsan est, ac viverra leo tellus eget enim. Donec vitae auctor nisl, interdum laoreet metus. Etiam ut ligula volutpat, ornare felis ac, pharetra neque. Nunc non mi sodales, rutrum enim ut, finibus magna. Aliquam erat volutpat. Nullam orci elit, scelerisque id lectus nec, lacinia efficitur nisi.', 'ISBN': '5930664514'}]

def test_db_fetch_multiple_results():
    sql = "SELECT * FROM FAVORITES WHERE USER_ID = 12345"
    query_object = db.dbQuery(sql)
    results = db.dbQuery.callDbFetch(query_object)
    assert results == [{'USER_ID': '12345', 'ISBN': '1234567890'}, {'USER_ID': '12345', 'ISBN': '1234667890'}, {'USER_ID': '12345', 'ISBN': '1244667890'}]






