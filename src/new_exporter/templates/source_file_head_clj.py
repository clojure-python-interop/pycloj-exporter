from string import Template
source_file_head = Template('''
(ns $clj_namespace
  "$docstring"
  (:require [libpython-clj.python
             :refer [import-module
                     get-item
                     get-attr
                     python-type
                     call-attr
                     call-attr-kw
                     att-type-map
                     ->py-dict
                     ->py-list
                     ]
             :as py]
            [clojure.pprint :as pp]))

(py/initialize!)
(defonce $clj_module_name (import-module "$namespace"))
''')
