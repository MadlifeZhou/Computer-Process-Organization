from collections import OrderedDict, namedtuple
import copy

event = namedtuple("Event", "clock node var val")
source_event = namedtuple("SourceEvent", "var val latency")


class DiscreEvent:
    def __init__(self, name="anonymous"):
        self.name = name
        self.inputs = OrderedDict()
        self.outputs = OrderedDict()
        self.nodes = []
        self.state_history = []
        self.event_history = []

    def input_port(self, name, latency=1):
        self.inputs[name] = latency

    def output_port(self, name, latency=1):
        self.outputs[name] = latency

    def add_node(self, name, function):
        node = Node(name, function)
        self.nodes.append(node)
        return node

    def _source_events2events(self, source_events, clock):

        events = []
        for se in source_events:
            # 遍历后相加
            source_latency = clock + se.latency + self.inputs.get(se.var, 0)

            if se.var in self.outputs:
                target_latency = self.outputs[se.var]
                events.append(event(clock=source_latency + target_latency,
                                    node=None, var=se.var,
                                    val=se.val, ))

            for node in self.nodes:
                if se.var in node.inputs:
                    target_latency = node.inputs[se.var]
                    events.append(event(clock=clock + source_latency + target_latency,
                                        node=node, var=se.var, val=se.val))

        return events

    def _pop_next_event(self, events):
        assert len(events) > 0
        events = sorted(events, key=lambda e: e.clock)
        event = events.pop(0)
        return event, events

    def _state_initialize(self):  # 将每个输入的变成None
        env = {}
        for var in self.inputs:
            env[var] = None
        return env

    def execute(self, *source_events, limit=100, events=None):
        """

        1. 先初始化状态
        2. 将输入的事件转化为列表
        3.
        """

        if events is None:
            events = []
        state = self._state_initialize()
        clock = 0

        self.state_history = [(clock, copy.copy(state))]

        while (len(events) > 0 or len(source_events) > 0) and limit > 0:
            limit -= 1
            new_events = self._source_events2events(source_events, clock)
            events.extend(new_events)
            if len(events) == 0: break
            event, events = self._pop_next_event(events)
            state[event.var] = event.val
            clock = event.clock
            source_events = event.node.activate(state) if event.node else []
            self.state_history.append((clock, copy.copy(state)))
            self.event_history.append(event)
        if limit == 0: print("limit reached")
        return state


class Node(object):
    def __init__(self, name, function):
        self.function = function
        self.name = name
        self.inputs = OrderedDict()
        self.outputs = OrderedDict()

    def __repr__(self):
        return "{} inputs: {} outputs: {}".format(self.name, self.inputs, self.outputs)

    def input(self, name, latency=1):
        assert name not in self.inputs
        self.inputs[name] = latency

    def output(self, name, latency=1):
        assert name not in self.outputs
        self.outputs[name] = latency

    def activate(self, state):

        args = []
        for v in self.inputs:
            args.append(state.get(v, None))
        res = self.function(*args)
        if not isinstance(res, tuple):
            res = (res,)
        output_events = []
        for var, val in zip(self.outputs, res):
            latency = self.outputs[var]
            output_events.append(source_event(var, val, latency))
        return output_events


if __name__ == '__main__':
    m = DiscreEvent("logic_not")
    m.input_port("A", 1)
    m.output_port("B", 1)
    n = m.add_node("not", lambda x: not x if isinstance(x, bool) else None)
    n.input("A", 1)
    n.output("B", 1)
    m.execute(source_event("A", True, 0),source_event("A", False, 5))
    print(m.state_history)

    a = {"c": 1}
    b = {'a': 1, "b": 2}
    c = {"d": 2}
    a.update(b)
    a.update(c)
    print(a)


