utils <- reticulate::import_from_path(module = "utils", path = "~/Desktop/projects/SpliceAI_AllDelta/spliceai/", convert = FALSE)
ann_m <- utils$Annotator_model()
get_spliceai <- function(SEQ, STRAND, ANN_M) {
  SEQ <- stringi::stri_trans_toupper(SEQ)
  stopifnot(stringi::stri_detect_regex(SEQ, "^[ATGCN]+$", max_count = 1L))
  stopifnot(STRAND %in% c("+", "-"))
  tibble::as_tibble(reticulate::py_to_r(utils$get_all_scores(SEQ, STRAND, ANN_M)), .name_repair = "minimal")
}
# get_spliceai("ATGCATCGGATCTAGCTTAGCTAGCTAGCTAGCT", "+", ann_m)

