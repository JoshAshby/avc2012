function(doc) {
  if(doc.doc_type == "botDoc"){
    emit(doc.id, doc);
}}
