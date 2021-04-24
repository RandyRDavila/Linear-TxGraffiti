



class linear_conjecture:
    
    def __init__(self, target, other, inequality, slope, y_intercept, properties = None, touch = 0.0):
        self.target = target
        self.other = other
        self.direction = inequality
        self.m = slope
        self.b = y_intercept
        self.hypothesis_properties = properties
        self.touch = touch
        self.graph_families = None
        
    def __repr__(self):
        
        if self.hypothesis_properties == None:
            if self.m == 1.0 or self.m == 1:
                if self.b == 0:
                    return f'If G is connected, then {self.target} {self.direction} {self.other}.'
                else:
                    return f'If G is connected, then {self.target} {self.direction} {self.other} + {self.b}.'
            else:
                if self.b == 0:
                    return f'If G is connected, then {self.target} {self.direction} {self.m}*{self.other}.'
                else:
                    return f'If G is connected, then {self.target} {self.direction} {self.m}*{self.other} + {self.b}.'
        
        elif len(self.hypothesis_properties) == 1:
            if self.m == 1.0 or self.m == 1:
                if self.b == 0:
                    return f'If G is connected and {self.hypothesis_properties[0]}, then {self.target} {self.direction} {self.other}.'
                else:
                    return f'If G is connected and {self.hypothesis_properties[0]}, then {self.target} {self.direction} {self.other} + {self.b}.'
            else:
                if self.b == 0:
                    return f'If G is connected and {self.hypothesis_properties[0]}, then {self.target} {self.direction} {self.m}*{self.other}.'
                else:
                    return f'If G is connected and {self.hypothesis_properties[0]}, then {self.target} {self.direction} {self.m}*{self.other} + {self.b}.'
        
        elif len(self.hypothesis_properties) == 2:
            if self.m == 1.0 or self.m == 1:
                if self.b == 0:
                    return f'If G is connected, {self.hypothesis_properties[0]}, and {self.hypothesis_properties[1]}, then {self.target} {self.direction} {self.other}.'
                else:
                    return f'If G is connected, {self.hypothesis_properties[0]}, and {self.hypothesis_properties[1]}, then {self.target} {self.direction} {self.other} + {self.b}.'
            else:
                if self.b == 0:
                    return f'If G is connected, {self.hypothesis_properties[0]}, and {self.hypothesis_properties[1]}, then {self.target} {self.direction} {self.m}*{self.other}.'
                else:
                    return f'If G is connected, {self.hypothesis_properties[0]}, and {self.hypothesis_properties[1]}, then {self.target} {self.direction} {self.m}*{self.other} + {self.b}.'
    

    def inequality(self):
        return [self.target, self.direction, self.m, self.other, self.b]
    
    def get_expression(self):
        return f'{self.target} {self.direction} {self.m}*{self.other} + {self.b}'
    
    def __eq__(self, other):
        return self.hypothesis_properties == other.hypothesis_properties and self.inequality() == other.inequality()
    
    