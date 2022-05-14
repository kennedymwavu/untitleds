# ----Errors----
# in base R, errors are thrown by `stop()`:
e <- function() {
  stop("This is an error message", call. = FALSE)
}

f <- function() {
  e()
}

g <- function() {
  f()
}

g()


# Unlike errors, you can have multiple warnings from a single function call:
fw <- function() {
  cat("1\n")
  warning("Warning W1")
  cat("2\n")
  warning("Warninig W2")
  cat("3\n")
  warning("Warning W3")
}

fw()

# Messages are displayed immediately:
fm <- function() {
  cat("1\n")
  message("Message M1")
  cat("2\n")
  message("Message M2")
  cat("3\n")
  message("Message M3")
}

fm()

# ----8.2.4----
# Write a wrapper around `file.remove()` that throws an error is the file to be
# deleted does not exist
remover <- function(x) {
  # Throw error if file doesn't exist:
  if ( !file.exists(x) ) {
    stop(
      paste0("File ", x, " not found!"),
      call. = FALSE
    )
  }

  # Otherwise delete the file:
  file.remove(x)
}

rm_files <- function(...) {
  to_delete <- c(...)

  if ( !is.null(to_delete) ) {
    purrr::map(
      .x = to_delete,
      .f = remover
    )
  }
}

# try to delete non-existing file:
rm_files("abc")

# create dummy file:
file.create("dummy1.R")

# Delete dummy file:
rm_files("dummy1.R")

# Good!

# try() let's you ignore an error and execution of function continues:
# normally:
f1 <- function(x) {
  log(x)
  10
}

# this would throw an error and stop fn execution:
f1("a")

# compared to:
f1 <- function(x) {
  try(log(x))
  10
}

f1("a")

