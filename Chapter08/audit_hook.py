# Add an auditing hook
typedef int (*hook_func)(const char *event, PyObject *args,
                         void *userData);
int PySys_AddAuditHook(hook_func hook, void *userData);

# Raise an event with all auditing hooks
int PySys_Audit(const char *event, PyObject *args);

# Internal API used during Py_Finalize() - not publicly accessible
void _Py_ClearAuditHooks(void);
