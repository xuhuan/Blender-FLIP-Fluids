/*
MIT License

Copyright (c) 2019 Ryan L. Guy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/

#ifndef FLUIDENGINE_FORCEFIELD_H
#define FLUIDENGINE_FORCEFIELD_H

#include "trianglemesh.h"
#include "meshobject.h"
#include "macvelocityfield.h"


class ForceField
{
public:
    ForceField();
    virtual ~ForceField() = 0;

    void updateMeshStatic(TriangleMesh meshCurrent);
    void updateMeshAnimated(TriangleMesh meshPrevious, 
                            TriangleMesh meshCurrent, 
                            TriangleMesh meshNext);

    void enable();
    void disable();
    bool isEnabled();

    void initialize(int isize, int jsize, int ksize, double dx);

    float getStrength();
    void setStrength(float s);

    float getFalloffPower();
    void setFalloffPower(float p);

    void enableMinDistance();
    void disableMinDistance();
    bool isMinDistanceEnabled();

    float getMinDistance();
    void setMinDistance(float d);

    void enableMaxDistance();
    void disableMaxDistance();
    bool isMaxDistanceEnabled();

    float getMaxDistance();
    void setMaxDistance(float d);
    
    virtual void update(double dt) = 0;
    virtual void addForceFieldToGrid(MACVelocityField &fieldGrid) = 0;
    virtual std::vector<vmath::vec3> generateDebugProbes() = 0;

protected:

    virtual void _initialize() = 0;

    int _isize = 0;
    int _jsize = 0;
    int _ksize = 0;
    double _dx = 1.0;
    bool _isInitialized = false;

    MeshObject _meshObject;

    float _strength = 0.0f;
    float _falloffPower = 1.0f;

    bool _isMinDistanceEnabled = false;
    float _minDistance = 0.0f;

    bool _isMaxDistanceEnabled = false;
    float _maxDistance = 0.0f;

};

#endif