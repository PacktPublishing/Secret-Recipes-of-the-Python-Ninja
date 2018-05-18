# Set the handler
typedef PyObject *(*hook_func)(PyObject *path)
int PyImport_SetOpenForImportHook(void *handler)

# Open a file using the handler
PyObject *PyImport_OpenForImport(const char *path)
