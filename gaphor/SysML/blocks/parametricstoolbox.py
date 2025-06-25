"""The definition for the parametric section of the toolbox."""

from gaphor import UML
from gaphor.core import gettext
from gaphor.diagram.diagramtoolbox import ToolDef, ToolSection, new_item_factory
from gaphor.SysML import diagramitems as sysml_items
from gaphor.UML import diagramitems as uml_items
from gaphor.UML.toolboxconfig import named_element_config


parametric_blocks = ToolSection(
    gettext("Parametric"),
    (
        ToolDef(
            "toolbox-connector",
            gettext("Connector"),
            "gaphor-connector-symbolic",
            "<Shift>C",
            new_item_factory(uml_items.ConnectorItem),
        ),
        ToolDef(
            "toolbox-constraint-block",
            gettext("Constraint Block"),
            "gaphor-constraint-block-symbolic",
            "o",
            new_item_factory(
                sysml_items.ConstraintBlockItem, config_func=named_element_config
            ),
        ),
    ),
)