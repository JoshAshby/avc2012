function(doc) {
  if(doc.doc_type == "heatDoc"){
    emit(doc._id, doc);

}}
