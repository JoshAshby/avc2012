function(doc) {
  if(doc.doc_type == "heatDoc"){
    emit(doc.heat, doc);

}}
