function(doc) {
  if(doc.doc_type == "adminDoc"){
    emit(doc.id, doc);
}}
