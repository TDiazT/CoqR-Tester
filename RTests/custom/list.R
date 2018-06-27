vector <- function(mode = "logical", length = 0L) .Internal(vector(mode, length))
logical <- function(length = 0L) .Internal(vector("logical", length))
character <- function(length = 0L) .Internal(vector("character", length))
integer <- function(length = 0L) .Internal(vector("integer", length))
structure <- function (.Data, ...)

{
    if(is.null(.Data))
        warning("Calling 'structure(NULL, *)' is deprecated, as NULL cannot have attributes.\n  Consider 'structure(list(), *)' instead.")
        ## to become: stop("attempt to set an attribute on NULL")
    attrib <- list(...)
    if(length(attrib)) {
        specials <- c(".Dim", ".Dimnames", ".Names", ".Tsp", ".Label")
        replace <- c("dim", "dimnames", "names", "tsp", "levels")
	m <- match(names(attrib), specials)
	ok <- (!is.na(m) & m)
	names(attrib)[ok] <- replace[m[ok]]
        ## prior to 2.5.0 factors would deparse to double codes
	if("factor" %in% attrib[["class", exact = TRUE]]
           && typeof(.Data) == "double")
            storage.mode(.Data) <- "integer"
	attributes(.Data) <- c(attributes(.Data), attrib)
    }
    .Data
}

argv <- list(structure(list(), .Names = character(0), row.names = integer(0), .S3Class = 'data.frame', class = structure('data.frame', package = 'methods')))
argv <- list(structure(function (x, mode = 'any') .Internal(as.vector(x, mode)), target = structure('ANY', class = structure('signature', package = 'methods'), .Names = 'x', package = 'methods'), defined = structure('ANY', class = structure('signature', package = 'methods'), .Names = 'x', package = 'methods'), generic = character(0), class = structure('MethodDefinition', package = 'methods')))
argv <- list(.Primitive('c'), list(list(), list(), list()), NULL)
{ list(1, b=2) }
argv <- list(structure(FALSE, .Tsp = c(1, 1, 1), class = 'ts'), structure(FALSE, .Tsp = c(1, 1, 1), class = 'ts'));list(argv[[1]],argv[[2]]);
argv <- list('‘', 'Matrix', '’');list(argv[[1]],argv[[2]],argv[[3]]);
{ f <- function(a = 2) { g(a) } ; g <- function(b) { missing(b) } ; f() }
structure('MethodDefinition', package = 'methods')
argv <- list(logical(0))
list(1:50, F)

list(a=1, 2, b=3)
list(a=1, list(list(list(2, bc=3))), 4, c=5)
list(1, list(), list(list()))